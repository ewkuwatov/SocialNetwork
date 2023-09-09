from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

comments_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])

@comments_router.post('/add_comments')
async def add_comments(data: CommentModel):
    pass

@comments_router.put('/edit_comments')
async def edit_comments(data: EditCommentModel):
    pass

@comments_router.delete('/delete_comments')
async def delete_comments(comment_id: int):
    pass

@comments_router.get('/get_comments')
async def get_comments(post_id: int):
    pass
