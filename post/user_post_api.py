from fastapi import APIRouter

user_router = APIRouter(prefix='/user_post', tags=['Работа с публикацией'])

@user_router.post('/public_post')
async def public_post():
    pass

@user_router.put('/change_post')
async def change_post():
    pass

@user_router.delete('/delete_post')
async def delete_post():
    pass

@user_router.get('/get_all_post')
async def get_all():
    pass

@user_router.post('/add_photo')
async def add_photo():
    pass

@user_router.delete('/delete_photo')
async def delete_photo():
    pass

