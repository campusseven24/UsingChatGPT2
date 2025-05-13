from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.v1 import router, user  # 각 라우터 임포트
from app.api.v1.router import api_router  # api_router 임포트

app = FastAPI()

# CORS 설정 (프론트엔드와 통신을 위한 허용 설정)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 실제 운영환경에서는 특정 도메인만 허용
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

API_V1_STR = "/api/v1"  # API 버전 설정 (유지보수성과 확장성이 뛰어나기 때문에 best practice)

# api_router는 보통 여러 서브 라우터(user, item 등)를 include_router한 상위 라우터
# prefix=API_V1_STR 설정으로 인해 /api/v1/...로 시작하는 URL 경로가 자동 생성됨.  /api/v1/users,  /api/v1/items 등
# tags=["API"]는 자동 문서화(Swagger UI 등)에서 그룹 이름으로 표시됨.
app.include_router(api_router, prefix=API_V1_STR, tags=["API"])  # api_router 등록


@app.get("/")
def read_root():
    return {"message": "Welcome to My FastAPI App"}
