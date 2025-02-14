import requests

URL = "https://api.notion.com/v1/pages"


class NotionAPI:
    def __init__(self, id=None, token: str = None, text_output: str = None):
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }
        payload = {
            "parent": {"database_id": id},
            "properties": {
                "名前": {
                    "title": [{"text": {"content": text_output}}],
                },
            },
        }
        response = requests.post(URL, json=payload, headers=headers)
        print(response)