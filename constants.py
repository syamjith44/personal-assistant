import os
from base64 import b64decode
from dotenv import load_dotenv


load_dotenv()


MODEL_PATH = b64decode(os.getenv("MODEL_PATH")).decode('utf-8')
PROMPT_PATH = b64decode(os.getenv("PROMPT_PATH")).decode('utf-8')
