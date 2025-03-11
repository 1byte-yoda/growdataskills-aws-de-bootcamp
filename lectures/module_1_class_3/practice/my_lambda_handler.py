import requests


def main(event, context):
    response = requests.get("https://google.com")
    print(response.text)
