from dotenv import load_dotenv
# from configs.llm_config import llm_Settings
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from controllers import chat2note_router

origins = [
    "*"
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 允许的域名
    allow_credentials=True,           # 允许携带凭证
    allow_methods=["*"],              # 允许的 HTTP 方法，如 GET, POST 等
    allow_headers=["*"],              # 允许的请求头
)


router = APIRouter()
router.include_router(chat2note_router, prefix="/chat2note", tags=["mark", "chat2note"])

app.include_router(router, prefix="/v1/api", tags=["mark"])

# print(llm_Settings.OPENAI_API_KEY)
if __name__ == "__main__":
  
  config = uvicorn.Config("app:app", host="0.0.0.0", port=9988, reload=True)
  server = uvicorn.Server(config)
  server.run()