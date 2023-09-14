from database import get_db
from database.models import Comment


# Опубликовать комментарий
def add_comment_db(post_id, text, user_id):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, comment_text=text, user_id=user_id)
    db.add(new_comment)
    db.commit()

    return "Комментарий оставлен"


# Удалить комментарий
def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удалено'

    return False

# Изменить определенный комментарий
def change_comment_db(comment_id, new_comment, user_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(comment_id=comment_id, user_id=user_id).first()

    if exact_comment:
        exact_comment.post_text = new_comment
        db.commit()

        return 'Комментарий изменен'

    return False