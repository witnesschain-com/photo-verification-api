from services.image_processor import ImageProcessor
from services.claude_service import ClaudeService
from schemas import ClassificationRequest, ClassificationResponse

class ClassificationService:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.claude_service = ClaudeService()

    async def classify_photos(self, request: ClassificationRequest) -> ClassificationResponse:
        try:
            # Process images
            image_contents = await self.image_processor.prepare_images(request.photos)
            
            # Get classification from Claude
            result = await self.claude_service.classify_photos(request.task, image_contents)
            
            return ClassificationResponse(
                classified=result["classified"],
                reason=result["reason"]
            )
        except Exception as e:
            return ClassificationResponse(
                classified=False,
                reason=f"Error processing request: {str(e)}"
            )