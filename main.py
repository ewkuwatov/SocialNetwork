from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from photo.photo_api import photo_router


app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(photo_router)

#Добавление ссылки для открытия локальных файлов
app.mount(path='/media', app=StaticFiles(directory='media'))

@app.get('/hello')
async def hello():
    return {'message': 'Hello world'}

