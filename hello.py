from flask import Flask
from markupsafe import escape
from flask import url_for

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

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

#permet d'afficher directement les données dans la console, au lancement de l'application (utile pour des tests)
with app.test_request_context():
    """
    affichage des adresses absolues des différentes méthodes utilisées dans l'application
    il est préférable d'utiliser url_for pour générer des liens plutôt que d'écrire les liens "en dur"
    """
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
