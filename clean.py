import pandas as pd
class cleaner:
    def __init__(self, value:list) -> None:
        from extract import Extract
        
        if len(value) > 1:
            raise ValueError("error")
        
        self.df = value[0] if not isinstance(value[0], str) else Extract(value[0]).dataframe()
    
    def List(self) ->None:
          for c in list(self.df.columns):
              if isinstance(self.df[c].iloc[0], list):
                  values = []
                  for i in self.df[c]:
                      values.append(i[0])
                  self.df[c] = values
                      
        
    def dict(self) -> pd.DataFrame:
        
        
            for c in list(self.df.columns):
                first_valid = self.df[c].dropna()

                if not first_valid.empty and isinstance(first_valid.iloc[0], dict):
                    df_new = pd.json_normalize(self.df[c]).add_prefix(f"{c}_")
                    self.df = pd.concat([self.df.drop(columns=[c]), df_new], axis=1)
                    
    def normalize(self) -> None:
        for c in list(self.df.columns):
            if isinstance(self.df[c].iloc[0], str):
                self.df[c] = self.df[c].str.lower().str.title().str.capitalize()
                
    def clean_column(self) -> None:
        
        for c in list(self.df.columns):
            
            if self.df[c].isna().mean() > 0.3:
                self.df = self.df.drop(columns=[c])
                
    def clean_line(self,line=None) -> None:
        
        self.df = self.df.fillna(line) if line is not None else self.df.dropna()
        
    def df_clean(self, values:list) ->pd.DataFrame:
        for i in values:
            match i:
                case "dict":
                    self.dict()
                case "normalize":
                    self.normalize()
                case "clean_column":
                    self.clean_column()
                case "clean_line":
                    if type(i) == dict:
                        self.clean_line(i.values())
                    else:
                        self.clean_line()
                case "list":
                    self.List()
                        
        return self.df
                        
        
                
        
        
    
        
    
    
    
    
    
