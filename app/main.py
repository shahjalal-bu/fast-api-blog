from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .schemas import Blog
from . import models
from .database import engine

#  create app

app = FastAPI()

#  create tables

models.Base.metadata.create_all(engine)

#  create db session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#  create blog
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog:Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#  get blog
@app.get("/blog")
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#  get blog by id
@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog(id:int,respnse:Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # respnse.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    return blog

#  update blog
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, blog:Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.update(blog)
    db.commit()
    return "updated"

#  delete blog
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"
