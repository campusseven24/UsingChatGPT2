# app/api/v1/router.py

from fastapi import APIRouter
from app.api.v1.endpoints import products  # 각 도메인 라우터 임포트

api_router = APIRouter()

# 하위 라우터들을 포함시킴
api_router.include_router(products.router, prefix="/products", tags=["products"])
