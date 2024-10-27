# lib/GetRequester.py
import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns the raw content of the response

    def load_json(self):
        response_body = self.get_response_body()
        return requests.get(self.url).json()  # Converts the JSON content into a Python dictionary or list
