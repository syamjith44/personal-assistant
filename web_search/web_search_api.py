import requests


class DuckDuckGo:
    BASE_URL = "https://api.duckduckgo.com/"

    def __init__(self, query_input):
        self.query_input = query_input
        self.call_api()
        self.results = self.get_search_results()

    def call_api(self):
        params = {"q": self.query_input, "format": "json"}
        self.response = requests.get(self.BASE_URL, params=params)
        self.response_data = self.response.json()
        return self.response_data
    
    def fetch_instant_answer(self):
        return self.response_data.get("AbstractText")
    
    def get_search_results(self):
        if self.response_data.get("AbstractText"):
            return [self.response_data.get("AbstractText")]
        elif self.response_data.get('RelatedTopics'):
            return [data.get('text', '') for data in self.response_data.get('RelatedTopics')]
        else:
            return []


