from fastapi import APIRouter

comments_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])

@comments_router.post('/add_comments')
async def add_comments():
    pass

@comments_router.put('/edit_comments')
async def edit_comments():
    pass

@comments_router.delete('/delete_comments')
async def delete_comments():
    pass

@comments_router.get('/get_comments')
async def get_comments():
    pass
