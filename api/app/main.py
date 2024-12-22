from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate):
    db = SessionLocal()
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    return crud.get_users(db, skip=skip, limit=limit)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    return crud.delete_user(db, user_id=user_id)