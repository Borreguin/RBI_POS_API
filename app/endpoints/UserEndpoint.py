from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from app import local_db
from app.schemas.UserSchema import UserCreate
from app.services import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post('/', response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(local_db)):
    db_user = UserService.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    return UserService.create_user(db=db, user=user)


# @app.get('/users/', response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(local_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#
#     return users
