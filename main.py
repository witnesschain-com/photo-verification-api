from fastapi import FastAPI, File, UploadFile
from typing import List
from services.verification_service import ClassificationService
from schemas import ClassificationRequest, ClassificationResponse

app = FastAPI()
verification_service = ClassificationService()

@app.post("/classify-photos/", response_model=ClassificationResponse)
async def classify_photos(
    task: str,
    photos: List[UploadFile] = File(...)
) -> ClassificationResponse:
    """
    classify if uploaded photos satisfy the given task using Claude
    
    Args:
        task: Description of what the photos should show/contain
        photos: List of image files to classify
    
    Returns:
        JSON response with verification result and reason
    """
    request = ClassificationRequest(task=task, photos=photos)
    return await verification_service.classify_photos(request)