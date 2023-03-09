from database import Base
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.types import ARRAY

from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


# class About(Base):
#     __tablename__ = 'about'
#     id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
#     name_en = Column(String, nullable=False)
#     updatedAt = Column(TIMESTAMP(timezone=True),
#                        default=None, onupdate=func.now())

class Project(Base):
    '''
    Store projects with translations and images
    '''
    __tablename__ = 'projects'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    title_en = Column(String, nullable=False)
    title_ru = Column(String, nullable=False)
    description_en = Column(String, nullable=False)
    description_ru = Column(String, nullable=False)
    images = ARRAY(str, as_tuple=False, dimensions=None, zero_indexes=False)
    build_stack = Column(String, nullable=False)
    github_link = Column(String, nullable=True)
    deploy_link = Column(String, nullable=True)
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
