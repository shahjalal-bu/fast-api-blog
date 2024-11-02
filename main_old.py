from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/post/{id}")
async def get_post(id:int):
    return {"id":id}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/blog")
async def create_blog(blog:Blog):
    return blog