import pandas as pd
class Products:
    def __init__(self) ->None:
        from extract import Extract
        from clean import cleaner
        self.df = cleaner([Extract("https://dummyjson.com/products?limit=0").dataframe()]).df_clean(["dict","normalize", "clean_column"])[['products_id','products_title', 'products_category','products_stock',  'products_price', 'products_discountPercentage','products_rating',  'products_availabilityStatus']]
        
        
        
    def df_product(self)->pd.DataFrame:
        return self.df
    

