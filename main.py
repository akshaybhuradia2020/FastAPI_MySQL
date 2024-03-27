from fastapi import FastAPI
from app.api.routers.users import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Test Application"}
