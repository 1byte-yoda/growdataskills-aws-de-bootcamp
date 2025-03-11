import requests


def main(event, context):
    response = requests.get("https://google.com")
    print(response.text)
    return {
        "status_code": 200,
        "event_json": event
    }
