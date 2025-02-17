import configparser
import requests

VALIDSETTINGS = "VALIDSETTINGS"
INVALIDSETTINGS = "INVALIDSETTINGS"
OLDVALIDSETTINGS = "OLDVALIDSETTINGS"
TOKEN = "token"
ID = "id"


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

    assert response.status_code == 400 or 401 or 404
    assert response.json()["object"] == "error"


def test_exist_url():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = f"https://api.notion.com/v1/databases/{config[VALIDSETTINGS][ID]}/query"
    headers = {
        "Authorization": f"Bearer {config[VALIDSETTINGS][TOKEN]}",
        "Notion-Version": "2022-06-28",
    }
    response = requests.post(url, headers=headers)
    assert response.status_code == 200
    assert response.json()["object"] == "list"


def test_not_exist_url():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = f"https://api.notion.com/v1/databases/{config[INVALIDSETTINGS][ID]}/query"
    headers = {
        "Authorization": f"Bearer {config[INVALIDSETTINGS][TOKEN]}",
        "Notion-Version": "2022-06-28",
    }
    response = requests.post(url, headers=headers)
    assert response.status_code == 400 or 401 or 404
    assert response.json()["object"] == "error"


def test_not_exist_invaild_url():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = f"https://api.notion.com/v1/databases/{config[INVALIDSETTINGS][ID]}/query"
    headers = {
        "Authorization": f"Bearer {config[INVALIDSETTINGS][TOKEN]}",
        "Notion-Version": "2022-06-28",
    }
    response = requests.post(url, headers=headers)
    assert response.status_code == 400 or 401 or 404
    assert response.json()["object"] == "error"
