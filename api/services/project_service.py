from typing import List
from api.schemas.project import ProjectSchema
from api.utils.helper import get_project_data

def get_projects() -> List[ProjectSchema]:
    projects = get_project_data()
    return [ProjectSchema(**vars(project)) for project in projects]
