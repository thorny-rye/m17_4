from fastapi import FastAPI, APIRouter
from routers import task, user
app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)