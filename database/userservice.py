from datetime import datetime

from database.models import User
from database import get_db


# Регистрация пользователя
def register_user_db(name, surname, email, phone_number, city, password):
    db = next(get_db())

    cheker = db.query(User).filter_by(email=email).first()

    if cheker:
        return False

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    city=city, password=password, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегистрирован'

# Вход в аккаунт
def login_get_db(email, password):
    db = next(get_db())

    cheker = db.query(User).filter_by(email=email).first()

    if cheker:
        if cheker.password == password:
            return cheker
        elif cheker.password != password:
            return 'Неверный пароль'

    return 'Ошибка в данных'

# Добавить фото профиля
def add_profile_photo_db(user_id, photo):
    db = next(get_db())

    cheker = db.query(User).filter_by(id=user_id).first()

    if cheker:
        cheker.profile_photo = photo
        db.commit()

        return 'фото профиля добавлено'

    return False


# Изменить данные
def change_info_db(user_id, edit_data, new_data):
    pass

# Удалить фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())

    cheker = db.query(User).filter_by(id=user_id).first()

    if cheker:
        cheker.profile_photo = 'None'
        db.commit()

        return 'фото профиля удалено'

    return False

# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


# Получить информацию про определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    return exact_user