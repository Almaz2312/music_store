from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.schemas.users import UserCreate
from db.sessions import get_db
from db.utils.users import create_new_user

router = APIRouter()


@router.post("/register/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
