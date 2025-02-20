import requests

from error import BadRequestError, UnauthorizedError, GeneralAPIError


class NotionAPI:

    def insert_database(self, id=None, token: str = None, text_output: str = None) -> str:
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
        try:
            self._check_token(token=token)
        except BadRequestError as b:
            return b
        except UnauthorizedError as u:
            return u
        except GeneralAPIError as g:
            return g
        response = requests.post(url, json=payload, headers=headers)

    def test_check_token(self, token:str) -> None:
        try:
            self._check_token(token=token)
            return True
        except BadRequestError as b:
            return b
        except UnauthorizedError as u:
            return u
        except GeneralAPIError as g:
            return g

    def _check_token(self, token: str) -> None:
        url = "https://api.notion.com/v1/users/me"
        headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return
        elif response.status_code == 401:
            raise UnauthorizedError("有効なトークンではありません (401 Unauthorized)")
        else:
            raise GeneralAPIError(f"APIエラーが発生しました: ステータスコード {response.status_code}")
