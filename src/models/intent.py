from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    intent: str
    responses: List[str]
