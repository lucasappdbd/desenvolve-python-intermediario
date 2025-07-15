from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User

def validate_user_password(username, password):
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password:
        return user
    else:
        return None

def user_exists(username):
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    return user

def create_user(username, password, remember=False, last_login=None, foto=None, bio=None):
    new_user = User(
        username=username,
        password=password,
        remember=remember,
        last_login=last_login if last_login else datetime.now(),
        foto=foto,
        bio=bio
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

from app.models.models import Post

def create_post(body, user):
    post = Post(body=body, author=user)
    db.session.add(post)
    db.session.commit()
    return post

def get_timeline(limit=5):
    return db.session.query(Post).order_by(Post.timestamp.desc()).limit(limit).all()