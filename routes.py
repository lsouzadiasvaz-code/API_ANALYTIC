
from fastapi import FastAPI
app = FastAPI()
@app.get("/sales")
def sales():
    from sell import Carts
    data = Carts().df_sales()
    return data.to_dict(orient="records")
