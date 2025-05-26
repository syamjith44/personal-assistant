from llama_cpp import Llama

from constants import MODEL_PATH, WEB_SEARCH_DECISION_PROMPT
from web_search.web_search_api import DuckDuckGo


class WebSearchDecisionAgent:
    INPUT_PREFIX = "### Input:"
    OUTPUT_PREFIX = "### Output:"
    DECISION_PROMPT = WEB_SEARCH_DECISION_PROMPT

    def __init__(self, chat_input):
        self.response = ""
        self.web_search_required = False
        self.chat_input = chat_input
        self.prompt_llma()
        self.mark_web_search_required()

    def get_model(self):
        return Llama(
            model_path=MODEL_PATH,
            n_ctx=2048, verbose=False
        )
    
    def get_decision_prompt(self):
        with open(self.DECISION_PROMPT, 'r') as file:
            return file.read()
    
    def prompt_llma(self):
        llm = self.get_model()
        response = llm(
            f"{self.get_decision_prompt()}\n"
            f"{self.INPUT_PREFIX} {self.chat_input}\n"
            f"{self.OUTPUT_PREFIX}", 
            max_tokens=25,
            stop=["###"]
        )
        self.response = response["choices"][0]["text"].strip()

    def mark_web_search_required(self):
        self.web_search_required = self.response.upper() == "[INTERNET_SEARCH_REQUIRED]"

    def build_prompt_for_web_results(self):
        search = DuckDuckGo(query_input=self.chat_input)
        web_content = '\n'.join(f"- {text}" for text in search.results)
        return f"Here are some content from the web: {web_content}"