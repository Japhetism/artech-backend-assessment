import random
import string
from app.models import Project as ProjectModel

def generate_alphanumeric_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_random_title():
    words = [
        "Data Analysis", "Web Development", "AI Research", 
        "Mobile App", "E-commerce Platform", "Social Network", 
        "Game Development", "Health Tracker", "Portfolio Site", 
        "Blog Platform", "Online Learning", "Travel Planner", 
        "Cyber Security", "Ad & Tourism", "Book-Keeping"
    ]
    return random.choice(words)

def create_project(project_id, title):
    sanitized_title = title.lower().replace(" ", "")
    description = f"{title} project description for {title} is a {title} with {title}."
    image_url = f"https://via.placeholder.com/150/0000FF/FFFFFF?text=Project+{sanitized_title}"
    project_url = f"http://{sanitized_title}.{project_id}.com/{sanitized_title}/{project_id}"

    return ProjectModel(
        id=project_id,
        title=title,
        description=description,
        image_url=image_url,
        project_url=project_url
    )

def get_project_data(num_projects=100):
    return [
        create_project(generate_alphanumeric_id(), get_random_title())
        for _ in range(num_projects)
    ]
