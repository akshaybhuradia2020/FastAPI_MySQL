from sqlalchemy import select
from app.api.models.users import User
from app.api.models.users_dto import UsersDTO
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user(_db: AsyncSession):
    return (await _db.scalars(select(User))).all()
    # return _db.query(SQL_USER).all()


async def check_user_exist(_db: AsyncSession, user: UsersDTO):
    return (
        await _db.scalars(select(User.email).where(User.email == user.email))
    ).first()
    # return _db.query(SQL_USER).filter(SQL_USER.email == user.email).first()


async def create_user(_db: AsyncSession, user: UsersDTO):
    db_user = User(
        id=user.id,
        email=user.email,
        gender=user.gender,
        fullname=user.fullname,
        isactive=user.isactive,
        passwd=user.passwd,
    )
    _db.add(db_user)
    await _db.commit()
    await _db.refresh(db_user)
    return db_user
