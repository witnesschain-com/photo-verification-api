from fastapi import FastAPI, File, UploadFile
from typing import List
from services.verification_service import VerificationService
from schemas import VerificationRequest, VerificationResponse

app = FastAPI()
verification_service = VerificationService()

@app.post("/verify-photos/", response_model=VerificationResponse)
async def verify_photos(
    task: str,
    photos: List[UploadFile] = File(...)
) -> VerificationResponse:
    """
    Verify if uploaded photos satisfy the given task using Claude
    
    Args:
        task: Description of what the photos should show/contain
        photos: List of image files to verify
    
    Returns:
        JSON response with verification result and reason
    """
    request = VerificationRequest(task=task, photos=photos)
    return await verification_service.verify_photos(request)