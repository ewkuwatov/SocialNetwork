from pydantic import BaseModel

class PublicPostModel(BaseModel):
    user_id: int
    post_text: str

class EditPostModel(BaseModel):
    post_id: int
    new_text: str
    user_id: int

