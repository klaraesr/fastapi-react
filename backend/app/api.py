from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.session import engine
from db.base import Base
from api.base import api_router


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
  
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}