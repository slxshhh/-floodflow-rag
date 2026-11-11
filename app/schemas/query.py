from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    query: str
    filter_dict: Optional[dict] = None
    