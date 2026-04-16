import pandas as pd
class Extract:
    def __init__(self, url:str) -> None:
        self.url = url
      
        
    def request(self) -> None:
        import requests
        self.requestData = requests.get(url=self.url).json()
        
    def dataframe(self) -> pd.DataFrame:
        self.request()
        return pd.DataFrame(self.requestData)
    
   

        
    
 