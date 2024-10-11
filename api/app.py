from fastapi import FastAPI
from dotenv import load_dotenv
from configs.llm_config import llm_Settings

print(llm_Settings.OPENAI_API_KEY)