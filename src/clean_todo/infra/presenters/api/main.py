from fastapi import FastAPI

from clean_todo.domain.entities.task import Task


app = FastAPI()


@app.get("/")
async def read_root() -> Task:
    return Task(name='Test')
