from app import app, db
from app.models.models import User, Post
from datetime import datetime

app.app_context().push()

## adicionando usuários
user = User(username='roberto', password='123', last_login=datetime.now())
db.session.add(user)
db.session.commit()

## adicionando posts
user = db.session.get(User, 1) # get usuário pelo seu id no banco
post = Post(body='olá mundo!', author=user, timestamp=datetime.now())
db.session.add(post)
db.session.commit()

# listando posts de um usuário
user = db.session.get(User, 1) # get usuário pelo seu id no banco
for post in user.posts: # itera no atributo de relacionamento
    print(post.id, post.body, post.user_id, post.author.username)