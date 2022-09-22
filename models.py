from enum import Enum
from typing import List, Optional
import uuid
from pydantic import BaseModel

class Gender(str,Enum):
    male = "male"
    female = 'female'

class Role(str,Enum):
    admin = "admin"
    user = 'user'
    student = "student"


class User(BaseModel):
    id: Optional[uuid.UUID]=uuid.uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role] 

class UpdateUserModel(BaseModel):
      first_name:Optional[str]
      last_name: Optional[str]
      middle_name: Optional[str]
      gender:Optional[Gender]
      roles:Optional[List[Role] ]
