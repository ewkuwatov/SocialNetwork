from fastapi import APIRouter, UploadFile

from database.userservice import add_profile_photo_db, delete_profile_photo_db


photo_router = APIRouter(prefix='/photo', tags=['Фотографии'])


#добавление фото
@photo_router.post('/add-photo')
async def add_user_photo(photo_file: UploadFile, user_id: int):
    # сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    result = add_profile_photo_db(user_id, photo=f'/media/{photo_file.filename}')


    return {'status': 1, 'message': result}

#Изменить фото
@photo_router.put('/edit-photo')
async def edit_profile_photo(user_id: int, new_photo_file: UploadFile):
    # сохранить локально фото
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()

        file.write(user_photo)

    result = add_profile_photo_db(user_id, photo=f'/media/{new_photo_file.filename}')

    return {'status': 1, 'message': result}

#Удалить фото
@photo_router.delete('/delete-photo')
async def delete_photo(user_id: int):
    result = delete_profile_photo_db(user_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователь не найден'}
