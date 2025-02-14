from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    anthropic_api_key: str = "your-key-here"
    model_name: str = "claude-3-opus-20240229"  # Updated to Opus
    max_tokens: int = 4096  # Increased token limit for Opus
    temperature: float = 0.5  # Added temperature for more controlled responses

    class Config:
        env_file = ".env"