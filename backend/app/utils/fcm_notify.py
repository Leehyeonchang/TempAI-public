import requests

FCM_KEY = "서버_KEY_입력"
FCM_URL = "https://fcm.googleapis.com/fcm/send"

def send_push_notification(token, title, message):
    headers = {
        "Authorization": f"key={FCM_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": token,
        "notification": {
            "title": title,
            "body": message
        }
    }
    requests.post(FCM_URL, json=payload, headers=headers)
