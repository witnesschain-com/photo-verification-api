from services.image_processor import ImageProcessor
from services.claude_service import ClaudeService
from schemas import VerificationRequest, VerificationResponse

class VerificationService:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.claude_service = ClaudeService()

    async def verify_photos(self, request: VerificationRequest) -> VerificationResponse:
        try:
            # Process images
            image_contents = await self.image_processor.prepare_images(request.photos)
            
            # Get verification from Claude
            result = await self.claude_service.verify_photos(request.task, image_contents)
            
            return VerificationResponse(
                verified=result["verified"],
                reason=result["reason"]
            )
        except Exception as e:
            return VerificationResponse(
                verified=False,
                reason=f"Error processing request: {str(e)}"
            )