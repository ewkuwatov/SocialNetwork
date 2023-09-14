from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel

posts_router = APIRouter(prefix='/user', tags=['Управление пользователями'])

@posts_router.post('/login')
async def login_user(data: LoginUserModel):
    pass

@posts_router.post('/register')
async def register_user(data: RegisterUserModel ):
    pass

@posts_router.put('/change_info')
async def change_info(data: EditUserModel):
    pass

@posts_router.get('/get_user')
async def get_user(user_id: int):
    pass
