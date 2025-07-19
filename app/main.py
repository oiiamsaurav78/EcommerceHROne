from fastapi import FastAPI
from app.routers import products, orders

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "FastAPI is running . Visit /docs to see API."}