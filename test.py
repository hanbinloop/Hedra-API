import json
import base64
import requests

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def test_voices():
    r = requests.get("http://localhost:8000/voices")
    resp = r.text
    print(resp)

def test_tasks():
    r = requests.get("http://localhost:8000/tasks")
    resp = r.text
    print(resp)

def test_delete_task(task_id):
    r = requests.delete(f"http://localhost:8000/tasks/{task_id}")
    resp = r.text
    print(resp)

def crop_face():
    data = {
        "input_image": image_to_base64("./static/avatar.jpeg"),
    }

    r = requests.post(
        "http://127.0.0.1:8000/crop-face", data=json.dumps(data)
    )

    resp = r.json()
    return resp["response_image"]

def create_task():
    data = {
        "text": "古北水镇的建筑风格体现了华北民居的特色",
        "avatar_image": crop_face(),
        "avatar_image_input": {
            "prompt": "穿着红衣服的中国男子",
            "seed": 3133
        },
        "audio_source": "tts",
        "voice_id": "JBFqnCBsd6RMkjVDRZzb"
    }

    r = requests.post(
        "http://127.0.0.1:8000/tasks", data=json.dumps(data)
    )
    resp = r.json()
    return resp["job_id"]

def upload_user_audio():
    file_path = "./static/audio.wav"
    files = {
        "file": open(file_path, "rb")
    }
    r = requests.post(
        "http://127.0.0.1:8000/upload_audio", files=files
    )
    resp = r.json()
    return resp["url"]

def user_audio_create_task():
    audio_url = upload_user_audio()
    data = {
        "text": "古北水镇的建筑风格体现了华北民居的特色",
        "avatar_image": crop_face(),
        "avatar_image_input": {
            "prompt": "穿着红衣服的中国男子",
            "seed": 3133
        },
        "audio_source": "audio",
        "voice_url": audio_url
    }
    r = requests.post(
        "http://127.0.0.1:8000/tasks", data=json.dumps(data)
    )
    resp = r.json()
    return resp["job_id"]

# print(user_audio_create_task())