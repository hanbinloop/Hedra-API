# -*- coding:utf-8 -*-


from datetime import datetime
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field
from fastapi import UploadFile

class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None


class AvatarImageInput(BaseModel):
    prompt: str = Field(description="The prompt for avatar image input", default="")
    seed: int = Field(description="The seed value for avatar image generation", default=3133)

class CustomModeGenerateParam(BaseModel):
    """Generate with Custom Mode"""
    text: str = Field(..., description="The main text content")
    avatar_image: str = Field(..., description="The crop-face base64, must be crop-face api return")
    avatar_image_input: AvatarImageInput = Field(description="Input parameters for avatar image generation")
    audio_source: str = Field(description="Source of the audio, e.g., 'tts' or 'audio', user upload audio select 'audio'", default="tts")
    voice_id: Optional[str] = Field(description="select input voice_id or voice_url", default=None)
    voice_url: Optional[str] = Field(description="select input voice_id or voice_url", default=None)

class CustomModeCropFaceParam(BaseModel):
    """CropFace with Custom Mode"""
    input_image: str = Field(..., description="The avatar image base64, Supported image format: .jpeg / .png / .webp")
