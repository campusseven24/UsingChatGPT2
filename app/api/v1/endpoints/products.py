# app/api/v1/endpoints/items.py

from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app import schemas, crud
#from app.api import deps


router = APIRouter()



@router.get("/{product_id}", response_model=schemas.Product)
def read_product(*, 
                 #db = Depends(deps.get_db), 
                 product_id: int):
    return schemas.Product(id=product_id, name="코튼 반팔 티셔츠", price=19900.00, 
                           image_url="https://example.com/image.jpg", category_id=1)




# 이 코드는 FastAPI를 사용하여 아이템 CRUD(Create, Read, Update, Delete) API를 구현한 것입니다.
# 각 API 엔드포인트는 SQLAlchemy 세션을 사용하여 데이터베이스와 상호작용합니다.