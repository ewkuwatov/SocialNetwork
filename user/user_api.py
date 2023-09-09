from fastapi import APIRouter

posts_router = APIRouter(prefix='/user', tags=['Управление пользователями'])

@posts_router.post('/login')
async def login_user():
    pass

@posts_router.post('/register')
async def register_user():
    pass

@posts_router.put('/change_info')
async def change_info():
    pass

@posts_router.get('/get_user')
async def get_user():
    pass
