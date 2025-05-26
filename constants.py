import os
from base64 import b64decode
from dotenv import load_dotenv


load_dotenv()


MODEL_PATH = b64decode(os.getenv("MODEL_PATH")).decode('utf-8')
PROMPT_PATH = b64decode(os.getenv("PROMPT_PATH")).decode('utf-8')
SYSTEM_PROMPT_PATH = b64decode(os.getenv("SYSTEM_PROMPT_PATH")).decode('utf-8')
WEB_SEARCH_DECISION_PROMPT = b64decode(os.getenv("WEB_SEARCH_DECISION_PROMPT")).decode('utf-8')
