from fastapi import APIRouter
from api.models.apiResponse import ApiResponse
from api.services.project_service import get_projects


router = APIRouter()

@router.get("/projects", response_model=ApiResponse)
async def fetch_projects():
    
    projects = get_projects()
    
    if not projects:
        return ApiResponse(
            status="fail",
            code=404,
            message="Unable to retrieve projects",
            data=[]
        )
    
    return ApiResponse(
        status="success",
        code=200,
        message="Projects retrieved successfully",
        data=projects
    )
