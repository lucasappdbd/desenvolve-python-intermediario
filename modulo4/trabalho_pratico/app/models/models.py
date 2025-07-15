from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text, Integer
from app import db
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    remember: Mapped[bool] = mapped_column(default=False)
    last_login: Mapped[datetime] = mapped_column()
    foto: Mapped[str] = mapped_column(String(255), nullable=True)
    bio: Mapped[str] = mapped_column(Text, nullable=True)

    # Relacionamento: um usuário pode ter vários posts
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Relacionamento reverso com User
    author: Mapped[User] = relationship("User", back_populates="posts")

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))




# from datetime import datetime
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import String, Text
# from app import db
# from flask_login import UserMixin
# from app import login

# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(String(100), nullable=False)
#     remember: Mapped[bool] = mapped_column(default=False)
#     last_login: Mapped[datetime] = mapped_column()
#     foto: Mapped[str] = mapped_column(String(255), nullable=True)
#     bio: Mapped[str] = mapped_column(Text, nullable=True)

# @login.user_loader
# def load_user(id):
#     return db.session.get(User, int(id))