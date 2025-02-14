import configparser
import requests

VALIDSETTINGS = "VALIDSETTINGS"
INVALIDSETTINGS = "INVALIDSETTINGS"
TOKEN = "token"


def test_token_vaild():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = "https://api.notion.com/v1/users/me"
    headers = {
        "Authorization": f"Bearer {config[VALIDSETTINGS][TOKEN]}",
        "Notion-Version": "2022-06-28",
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["object"] == "user"


def test_token_invaild():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = "https://api.notion.com/v1/users/me"
    headers = {
        "Authorization": f"Bearer {config[INVALIDSETTINGS][TOKEN]}",
        "Notion-Version": "2022-06-28",
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 401 or 404
    assert response.json()["object"] == "error"
