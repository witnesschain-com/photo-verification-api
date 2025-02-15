from pydantic import BaseModel
from fastapi import UploadFile
from typing import List

class ClassificationRequest:
    def __init__(self, task: str, photos: List[UploadFile]):
        self.task = task
        self.photos = photos

class ClassificationResponse(BaseModel):
    classified: bool
    reason: str
