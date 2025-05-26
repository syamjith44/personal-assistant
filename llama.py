from llama_cpp import Llama


class LlamaChat:
    USER_PREFIX = "### Human:"
    ASSISTANT_PREFIX = "### Assistant:"
    PROMPT_FILE = "tmp/prompt.txt"
    BASE_PROMPT = """
    ### System: You are TinyLLaMA, a helpful, concise, and friendly AI assistant.
    ### Respond clearly and conversationally.
    """

    def __init__(self, chat_input, exit=False):
        self.response = ""
        self.chat_input = chat_input
        self.prompt_llma()
        if exit is True:
            self.clear_context()

    def get_model(self):
        return Llama(
            model_path="models/tinyllama.gguf",
            n_ctx=2048, verbose=False
        )
    
    def update_context(self, prompt):
        with open(self.PROMPT_FILE, 'a') as file:
            file.write(f"{prompt}\n")
    
    def get_prompt(self):
        prompt = f"{self.USER_PREFIX} {self.chat_input}"
        self.update_context(prompt)
        with open(self.PROMPT_FILE, 'r') as file:
            return file.read()
    
    def prompt_llma(self):
        llm = self.get_model()
        _prompt = self.get_prompt()
        response = llm(
            f"{self.BASE_PROMPT}\n{_prompt}\n{self.ASSISTANT_PREFIX}", 
            max_tokens=1000,
            stop=["###"]
        )
        self.response = response["choices"][0]["text"].strip()
        self.update_context(f"{self.ASSISTANT_PREFIX} {self.response}")

    def clear_context(self):
        with open(self.PROMPT_FILE, 'w') as file:
            file.write("")
