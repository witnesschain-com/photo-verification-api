from anthropic import Anthropic
from typing import Dict, List
import json
from config import Settings

class ClaudeService:
    def __init__(self):
        settings = Settings()
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.model = settings.model_name
        self.max_tokens = settings.max_tokens

    def prepare_message_content(self, task: str, image_contents: List[Dict]) -> List[Dict]:
        message_content = [
            {
                "type": "text",
                "text": f"Please verify if these photos satisfy the following task: {task}\n"
                "Respond with JSON only in this format: {{\"verified\": boolean, \"reason\": string}}"
            }
        ]
        message_content.extend(image_contents)
        return message_content

    async def verify_photos(self, task: str, image_contents: List[Dict]) -> Dict:
        message_content = self.prepare_message_content(task, image_contents)
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": message_content
                }
            ]
        )
        
        return json.loads(response.content[0].text)