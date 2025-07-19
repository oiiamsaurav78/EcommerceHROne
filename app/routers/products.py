from fastapi import APIRouter, Query
from app.database import products_collection
from app.schemas import ProductModel
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
def create_product(product: ProductModel):
    result = products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id), **product.dict()}

@router.get("/products")
def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    products = products_collection.find(query).skip(offset).limit(limit)
    return [{"id": str(p["_id"]), **p} for p in products]
