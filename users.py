import pandas as pd
class Users:
    def __init__(self)->None:
        from extract import Extract
        from clean import cleaner
        self.df = cleaner([Extract("https://dummyjson.com/users?limit=0").dataframe()]).df_clean(["dict"])[['users_id',  'users_firstName', 'users_lastName', 'users_age', 'users_gender','users_company.address.country', 'users_company.address.city','users_company.address.address']]
        
    
    def df_user(self) -> pd.DataFrame:
        self.df["users_name"] = self.df['users_firstName'] + " " + self.df['users_lastName']
        self.df = self.df.drop(columns=["users_firstName", "users_lastName"])
        return self.df[['users_id', 'users_name', 'users_age', 'users_gender','users_company.address.country', 'users_company.address.city','users_company.address.address']]
        
    
    
