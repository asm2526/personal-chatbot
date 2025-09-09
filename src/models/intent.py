"""
Intent model definition.
This pydantic model validates request/response data for intents,
and also provides Swagger documentation with an example
"""

from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    # name of the intent
    intent: str

    # List of possible bot responses for this intent
    responses: List[str]

    class Config:
        # Example shown in Swagger UI
        schema_extra = {
            "example": {
                "intent": "hello",
                "responses": ["Hi there!", "Hello!", "Hey!"]
            }
        }
