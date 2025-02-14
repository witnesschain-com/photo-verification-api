from fastapi import UploadFile
import base64
from typing import List, Dict

class ImageProcessor:
    @staticmethod
    async def encode_image(file: UploadFile) -> str:
        contents = await file.read()
        return base64.b64encode(contents).decode('utf-8')
    
    @staticmethod
    async def prepare_images(photos: List[UploadFile]) -> List[Dict]:
        image_contents = []
        for photo in photos:
            base64_image = await ImageProcessor.encode_image(photo)
            image_contents.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": photo.content_type,
                    "data": base64_image
                }
            })
        return image_contents