"""
Intent model definition.
This pydantic model validates request/response data for intents,
and also provides Swagger documentation with an example
"""

from pydantic import BaseModel
from typing import List, Optional

class Intent(BaseModel):
    # name of the intent
    intent: str
    # List of possible bot responses for this intent
    responses: List[str]
    examples: Optional[List[str]] = []

    class Config:
        # Example shown in Swagger UI
        json_schema_extra = {
            "example": {
                "intent": "weather",
                "responses": ["It's sunny!", "Looks like rain!"],
                "examples": ["how's the weather", "what's the forecast"]
                
            }
        }
