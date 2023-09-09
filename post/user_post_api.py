from fastapi import APIRouter, UploadFile, Body

from post import PublicPostModel, EditPostModel

user_router = APIRouter(prefix='/user_post', tags=['Работа с публикацией'])

@user_router.post('/public_post')
async def public_post(data: PublicPostModel):
    pass

@user_router.put('/change_post')
async def change_post(data: EditPostModel):
    pass

@user_router.delete('/delete_post')
async def delete_post(post_id: int, user_id: int):
    pass

@user_router.get('/get_all_post')
async def get_all():
    pass

@user_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None):
    pass

@user_router.delete('/delete_photo')
async def delete_photo(photo_id: int, user_id: int):
    pass

