from flask import render_template, request, redirect, url_for, flash
from app import app, alquimias
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
def index():
    user = current_user if current_user.is_authenticated else None
    posts = alquimias.get_timeline() if user else None
    return render_template('index.html', title='Página inicial', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()
        user = alquimias.validate_user_password(username, password)

        if user:
            flash("Login bem-sucedido!")
            login_user(user, remember=user.remember)
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválidos")
            return redirect(url_for('login'))

    return render_template('login.html', title='Login')

@app.route('/cadastro', methods=['GET'])
def cadastro_form():
    return render_template("cadastro.html", title='Cadastro')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    username = request.form['username'].lower()
    if alquimias.user_exists(username):
        flash("Usuário já existe!")
        return redirect(url_for('cadastro_form'))

    password = request.form['password'].lower()
    remember = True if request.form.get('remember') == 'on' else False
    foto = request.form.get('foto')
    bio = request.form.get('bio')

    user = alquimias.create_user(username, password, remember, foto=foto, bio=bio)
    login_user(user, remember=remember)
    return redirect(url_for("index"))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        alquimias.create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')