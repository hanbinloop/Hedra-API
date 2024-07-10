# -*- coding:utf-8 -*-

import json

from fastapi import Depends, FastAPI, HTTPException, status, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import schemas
from deps import get_token
from utils import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_root():
    return schemas.Response()

@app.get("/voices")
async def fetch_voices(token: str = Depends(get_token)):
    '''
    Get the list of selectable audio provided by the system
    '''
    try:
        resp = await get_voices(token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/upload_audio")
async def upload_audio(
    file: UploadFile = File(...), token: str = Depends(get_token)
):
    '''
    Upload custom audio (Supported formats: .mp3 / .wav)
    '''
    try:
        resp = await upload(file, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/crop-face")
async def crop_face(
    data: schemas.CustomModeCropFaceParam, token: str = Depends(get_token)
):
    '''
    Upload image to crop face area (Supported formats: .jpeg / .png / .webp)
    '''
    try:
        resp = await get_crop_face(data.model_dump(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/tasks")
async def create_task(
    data: schemas.CustomModeGenerateParam, token: str = Depends(get_token)
):
    '''
    Create a task
    '''
    try:
        resp = await create_single_task(data.model_dump(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/tasks")
async def fetch_tasks(token: str = Depends(get_token)):
    '''
    Query tasks
    '''
    try:
        resp = await get_tasks(token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str, token: str = Depends(get_token)):
    '''
    Delete a task
    '''
    try:
        resp = await del_task(task_id, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
