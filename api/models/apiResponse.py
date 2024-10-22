from pydantic import BaseModel
from typing import List
from api.schemas.project import ProjectSchema

class ApiResponse(BaseModel):
    status: str
    code: int
    message: str
    data: List[ProjectSchema]
