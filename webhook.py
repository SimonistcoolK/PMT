import requests
def suggest(msg):
    webhook_url = "https://discord.com/api/webhooks/1484952738365182154/c6Mi8xqGp9-yMRJA7bgP8QzwXckd6GCEcMzejJyjfCpYeU9qYrnz5MB5VxFYAHSX7z21"
    data = {
        "content": msg
    }
    response = requests.post(webhook_url, json=data)

def send(url, msg):
    data = {
        "content": msg
    }
    requests = requests.post(url, json=data)