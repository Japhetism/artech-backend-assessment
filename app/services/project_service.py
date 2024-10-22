from typing import List
from app.schemas.project import ProjectSchema
from app.utils.helper import get_project_data

def get_projects() -> List[ProjectSchema]:
    projects = get_project_data()
    return [ProjectSchema(**vars(project)) for project in projects]
