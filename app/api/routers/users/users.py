from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.crud.users import users
from app.api.models.users_dto import UsersDTO
from app.api.config.db_conn import get_db
router = APIRouter(
    tags=["users"],
)



@router.post("/signup")
async def _create_user(user: UsersDTO, db: AsyncSession = Depends(get_db)):
    db_user = await users.check_user_exist(db, user=user)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await users.create_user(db, user=user)

@router.get("/get_all_user")
async def _get_all_user(db: AsyncSession = Depends(get_db)):
    _db_user = await users.get_user(db)
    return _db_user