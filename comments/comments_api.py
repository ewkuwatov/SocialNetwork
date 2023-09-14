from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

from database.commentservice import change_comment_db, add_comment_db, delete_comment_db, get_post_comments

comments_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])

@comments_router.post('/add_comments')
async def add_comments(data: CommentModel):
    result = add_comment_db(**data.model_dump())

    return {'status': 1, 'message': result}



@comments_router.put('/edit_comments')
async def edit_comments(data: EditCommentModel):
    result = change_comment_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Комментарий не найден'}


@comments_router.delete('/delete_comments')
async def delete_comments(comment_id: int):
    result = change_comment_db(comment_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Комментарий не найден'}



@comments_router.get('/get_comments')
async def get_comments(post_id: int):
    result = get_post_comments(post_id)

    return {'status': 1, 'message': result}
