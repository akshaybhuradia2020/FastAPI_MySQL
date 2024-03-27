from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.api.config.settings import MYSQL_DATABASE_URL

engine = create_async_engine(MYSQL_DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, autoflush=False)


async def get_db():
    db = async_session
    try:
        async with db() as session:
            yield session
    except:
        raise
    finally:
        await session.close()
