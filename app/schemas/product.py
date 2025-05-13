from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., max_length=100, example="코튼 반팔 티셔츠")
    price: float = Field(..., gt=0, example=19900.00)
    image_url: Optional[HttpUrl] = Field(None, example="https://example.com/image.jpg")
    category_id: Optional[int] = Field(None, example=1)


class ProductCreate(ProductBase):
    """
    상품 생성 시 사용할 스키마
    """
    pass


class ProductUpdate(ProductBase):
    """
    상품 수정 시 사용할 스키마 (부분 업데이트용이면 Optional 처리 필요)
    """
    name: Optional[str] = Field(None, max_length=100)
    price: Optional[float] = Field(None, gt=0)
    image_url: Optional[HttpUrl] = None
    category_id: Optional[int] = None

class ProductInDB(ProductBase):
    """
    DB 저장 시 사용할 스키마
    """
    id: int
    category_id: int

    class Config:
        orm_mode = True

class Product(ProductBase):
    """
    DB 조회 시 응답용 스키마
    """
    id: int

    class Config:
        orm_mode = True
