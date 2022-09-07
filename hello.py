from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    #pour éviter l'injection de code malveillant en exécutant un url de ce type : http://localhost:5000/<script>alert("bad")</script>
    return f"<p>Hello, {escape(name)}</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
#l'adresse canonique pour la page "/projects" a un "/" à la fin
#/about => redirection vers l'adresse canonique
def projects():
    return 'The project page'

#l'adresse canonique pour la page "/about" n'a pas "/" à la fin
#/about/ = erreur 404
@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
def index():
    return 'index'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


def show_the_login_form():
    """
    permet d'afficher un formulaire HTML
    """
    return """
    <form method="POST" action="/login">
        <label for="login">Login</label>
        <input type="text" name="login"/>
        <label for="pwd">Password</label>
        <input type="password" name="pwd"/>
        <input type="submit" value="submit">
    </form>
    """
    
def do_the_login():
    return """
    <p>Connexion</p>
    """

# @app.get('/login')
# def login_get():
#     return show_the_login_form()    

# @app.post('/login')
# def login_post():
#     return do_the_login()

#Les 2 méthodes ci-dessus (gestion de GET et POST dans 2 routes séparées)
#équivalent à la méthode ci-dessous (gestion de GEST et POST dans une route unique)
#
#2 routes différentes pour 2 méthodes HTTP différentes
# @app.get('/login')
# def login_get():
#     return show_the_login_form()    

# @app.post('/login')
# def login_post():
#     return do_the_login()

#1 route unique pour 2 méthodes HTTP différentes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#permet d'afficher directement les données dans la console, au lancement de l'application (utile pour des tests)
with app.test_request_context():
    """
    affichage des adresses absolues des différentes méthodes utilisées dans l'application
    il est préférable d'utiliser url_for pour générer des liens plutôt que d'écrire les liens "en dur"
    """
    print(url_for('index'))
    print(url_for('login'))#ne fonctionne pas si 2 routes "/login" existent (GET et POST)
    print(url_for('login', next='/'))#ne fonctionne pas si 2 routes "/login" existent (GET et POST)
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='css/style.css'))#résolution dynamique du chemin vers le fichier /static/css/style.css