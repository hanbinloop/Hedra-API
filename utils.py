import json
import os
import time

import aiohttp
from aiohttp import FormData
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

COMMON_HEADERS = {
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer": "https://www.hedra.com",
    "Origin": "https://www.hedra.com",
}


async def fetch(url, headers=None, data=None, method="POST", resp_format="json", file=None):
    import base64
    if headers is None:
        headers = {}
    headers.update(COMMON_HEADERS)
    if data is not None:
        data = json.dumps(data)

    form = None
    if file is not None:
        form = FormData()
        file_content = await file.read()
        form.add_field('file', file_content,
                       filename=file.filename,
                       content_type=file.content_type)
        headers.pop("Content-Type", None)

    # print(data, method, headers, url)

    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(
                method=method, url=url, data=form if form else data, headers=headers
            ) as resp:
                if resp_format == "json":
                    return await resp.json()
                else:
                    return await resp.text()
        except Exception as e:
            return f"An error occurred: {e}"


async def get_voices(token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/app/v1/app/setup"
    response = await fetch(api_url, headers, method="GET")
    return response

async def upload(file, token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/app/v1/app/avatars/audio"
    response = await fetch(api_url, headers, file=file)
    return response

async def create_single_task(data, token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/app/v1/app/avatars/predict-async"
    response = await fetch(api_url, headers, data)
    return response

async def get_crop_face(data, token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/upsample/v1/crop-face"
    response = await fetch(api_url, headers, data, resp_format="text")
    return {"response_image": response}

async def get_tasks(token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/app/v1/app/projects"
    response = await fetch(api_url, headers, method="GET")
    return response

async def del_task(task_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{BASE_URL}/api/app/v1/app/projects/{task_id}"
    response = await fetch(api_url, headers, method="DELETE")
    return response
