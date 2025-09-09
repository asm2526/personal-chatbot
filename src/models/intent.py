from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    intent: str
    responses: List[str]

    class Config:
        schema_extra = {
            "example": {
                "intent": "hello",
                "responses": ["Hi there!", "Hello!", "Hey!"]
            }
        }
