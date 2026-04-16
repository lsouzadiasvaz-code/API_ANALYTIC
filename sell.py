import pandas as pd
from clean import cleaner
class Carts:
    def __init__(self)->None:
        from extract import Extract
        from clean import cleaner
       
        self.df = cleaner([Extract("https://dummyjson.com/carts?limit=0").dataframe()]).df_clean(["dict", "list", "dict"])
    def df_sell(self)->None:
        self.df = self.df.rename(columns={"id": "carts_id", "total": "carts_total"})
        
        self.df = self.df[["carts_id", "carts_userId", "carts_products_id", "carts_products_quantity","carts_products_price", "carts_products_total"]]
        
    def df_sales(self) ->None:
        from users import Users
        from products import Products
        product = Products().df_product()
        user = Users().df_user()
        self.df_sell()
        self.df = self.df.merge(
            user[['users_id', 'users_name', 'users_age', 'users_gender','users_company.address.country', 'users_company.address.city']],
            left_on='carts_userId',
            right_on='users_id',
            how="left"
        )
        self.df = self.df.merge(
            product[["products_id", "products_title", "products_category"]],
            left_on="carts_products_id",
            right_on="products_id",
            how="left"
        )
           
                
        
        return self.df[[
            'users_name',
            'users_age',
            'users_gender',
            'users_company.address.country',
            'users_company.address.city',
            'products_title',
            'products_category',
            'carts_products_price',
            'carts_products_quantity',
            'carts_products_total'
        ]].rename(columns={
            'users_name': 'user_name',
            'users_age': 'user_age',
            'users_gender': 'user_gender',
            'users_company.address.country': 'country',
            'users_company.address.city': 'city',
            'products_title': 'product_name',
            'products_category': 'category',
            'carts_products_price': 'price',
            'carts_products_quantity': 'quantity',
            'carts_products_total': 'total'
        })
                
