from datetime import datetime

from database.models import UserPost, PostPhoto
from database import get_db


def add_post_db(user_id, post_text):
    db = next(get_db())

    new_post = UserPost(user_id=user_id,
                        post_yexy=post_text,
                        publish_date=datetime.now())

    db.add(new_post)
    db.commit()

    return 'Успешно добавлено'


def add_post_photo_db(post_id, photo):
    db = next(get_db())

    new_post_photo = PostPhoto(post_id=post_id, post_photo=photo)

    db.add(new_post_photo)
    db.commit()

    return 'фотографии загружены'


def edit_post_db(post_id, user_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id, user_id=user_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return "Успешно изменено"

    return False

def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()

        return "Успешно удалено"

    return False

def get_all_posts_db():
    db = next(get_db())

    all_posts = db.query(UserPost).all()

    return all_posts


def get_exact_posts_db():
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    if exact_post:
        return exact_post

    return False