from pydantic import BaseModel

class LoginUserModel(BaseModel):
    email: str
    password: str


class RegisterUserModel(BaseModel):
    name = str
    surname = str
    email = str
    phone_number = str
    city = str
    profile_photo = str
    password = str


class EditUserModel(BaseModel):
    user_id: int
    edit_data: str
    new_data: str
