from fastapi import FastAPI
import models
import projects as projects_endpoint
import uvicorn
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio Backend", version="0.0.1")
app.include_router(projects_endpoint.router, tags=['Projects'], prefix='/projects')


@app.get("/")
async def index():
    return {"status": True, "detail": "Hello, this is a backend for Stephan Zhdanov's portfolio web site!"}


@app.get("/about")
async def index():
    # Hardcoded for now
    return {"status": True, "detail": {
        "name": "Stephan Zhdanov",
        "status": "Software Engineer",
        "interests": "Interesetd in: Machine Learning, Data Science, Computer Vision, Microcontrollers Firmware Development, Web Backend. Learning web FrontEnd via study projects. I advocate open source and develop open source projects myself. True linux user!",
        "github": "ret7020",
        "telegram": "Rtyrdv"
    }}


# @app.get("/tech_stack")
# async def index():
#     # Hardcoded for now
#     return {"status": True, "detail": {
#         "directions": [{"name": "Python", "info": "Dev"}]
#     }}


# @app.get("/projects")
# async def index():
#     return {"status": True, "detail": "Projects placeholder"}


# @app.get("/hackathons")
# async def index():
#     return {"status": True, "detail": "Hackathons placeholder"}


# @app.get("/blogs")
# async def index():
#     return {"status": True, "detail": "Hackathons placeholder"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
