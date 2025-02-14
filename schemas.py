from pydantic import BaseModel
from fastapi import UploadFile
from typing import List

class VerificationRequest:
    def __init__(self, task: str, photos: List[UploadFile]):
        self.task = task
        self.photos = photos

class VerificationResponse(BaseModel):
    verified: bool
    reason: str
