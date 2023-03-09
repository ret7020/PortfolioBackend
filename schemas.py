from datetime import datetime
from typing import List
from pydantic import BaseModel


class ProjectSchema(BaseModel):
    id: str | None = None
    title_en: str
    title_ru: str
    description_en: str
    description_ru: str
    images = list
    build_stack: str
    github_link: str | None = None
    deploy_link: str | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

# class ProjectsResponse(BaseModel):
#     status: bool
#     detail: dict