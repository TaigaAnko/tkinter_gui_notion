import requests

class NotionAPI:
    def __init__(self, id=None, token=None, text_output=None) -> str:
        url = "https://api.notion.com/v1/pages"
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
        response = requests.post(url, json=payload, headers=headers) 

        result_dict = response.json()
        result = result_dict["object"]
        return result