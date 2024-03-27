from pydantic import BaseModel

class UsersDTO(BaseModel):
    id: int
    isactive: bool
    gender: str
    email: str
    fullname: str
    passwd: str
    
    class Config:
        from_attributes=True
        # orm_mode=True