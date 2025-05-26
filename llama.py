from llama_cpp import Llama

from constants import MODEL_PATH, PROMPT_PATH, SYSTEM_PROMPT_PATH


class LlamaChat:
    USER_PREFIX = "### Human:"
    ASSISTANT_PREFIX = "### Assistant:"
    PROMPT_FILE = PROMPT_PATH
    SYSTEM_PROMPT = SYSTEM_PROMPT_PATH

    def __init__(self, chat_input, exit=False, web_content=None):
        self.response = ""
        self.chat_input = chat_input
        self.web_content = web_content
        self.prompt_llma()
        if exit is True:
            self.clear_context()

    def get_model(self):
        return Llama(
            model_path=MODEL_PATH,
            n_ctx=2048, verbose=False
        )
    
    def get_system_prompt(self):
        with open(self.SYSTEM_PROMPT, 'r') as file:
            return file.read()
    
    def update_context(self, prompt):
        with open(self.PROMPT_FILE, 'a') as file:
            file.write(f"{prompt}\n")
    
    def get_prompt(self):
        prompt = f"{self.USER_PREFIX} {self.chat_input}"
        if self.web_content:
            prompt = f"\n### System: {self.web_content}\n{prompt}"
        self.update_context(prompt)
        with open(self.PROMPT_FILE, 'r') as file:
            return file.read()
    
    def prompt_llma(self):
        llm = self.get_model()
        _prompt = self.get_prompt()
        response = llm(
            f"{self.get_system_prompt()}\n{_prompt}\n{self.ASSISTANT_PREFIX}", 
            max_tokens=1000,
            stop=["###"]
        )
        self.response = response["choices"][0]["text"].strip()
        self.update_context(f"{self.ASSISTANT_PREFIX} {self.response}")

    def clear_context(self):
        with open(self.PROMPT_FILE, 'w') as file:
            file.write("")
