from pydantic import BaseModel

class ProjectSchema(BaseModel):
    id: str
    title: str
    description: str
    image_url: str
    project_url: str
