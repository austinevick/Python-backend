from http.client import HTTPException
from logging import root
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, UpdateUserModel, User

app = FastAPI()

db: List[User]= [
    User(id=uuid4(),
    first_name="Victor",
    last_name="Austine",
    middle_name="E",
    roles=[Role.admin],
    gender=Gender.male),
    User(id=uuid4(),
    first_name="Mary",
    last_name="Austine",
    middle_name="A",
    roles=[Role.user],
    gender=Gender.female)
]

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user.id:
            db.remove(user)
            return "user deleted successfully"
        raise HTTPException(status_code=404,
        detail=f"user with id: {user_id} does not exist")

@app.put("/api/v1/users/{user_id}")
async def updateUser(update_user: UpdateUserModel,user_id: UUID):
    for user in db:
        if user.id == user_id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
                if update_user.middle_name is not None:
                    user.middle_name = update_user.middle_name
                    if update_user.roles is not None:
                        user.roles = update_user.roles
                        return "user updated successfully"
            raise HTTPException(status_code=404,
        detail=f"user with id: {user_id} does not exist")

