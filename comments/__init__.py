from pydantic import BaseModel

class CommentModel(BaseModel):
    comment_text: str
    user_id: int

class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int

