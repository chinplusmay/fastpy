from fastapi import APIRouter, Depends
from app.schemas.user_schema import User

from sqlalchemy.orm import Session

from app.databases.session import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
router = APIRouter()




@router.post("/users") 
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    db_user = User(name = user.name, age = user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user



@router.get("/users/{user_id}")
def get_users(db : Session = Depends(get_db)):

    users = db.query(User).all()

    return users