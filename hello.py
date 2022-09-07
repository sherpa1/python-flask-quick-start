from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    '''
    Affiche dynamiquement un contenu en fonction
    de la variable <name> renseignée dans l'url.
    Tester l'URL http://localhost:5000/world
    '''
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):
    '''
    Affiche dynamiquement un contenu en fonction
    de la variable <username> renseignée dans l'url.
    Tester l'URL http://localhost:5000/user/john-doe
    '''
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    '''
    Affiche dynamiquement un contenu en fonction
    de la variable <post_id> renseignée dans l'url
    et convertie sous forme d'entier
    Tester l'URL http://localhost:5000/posts/777
    '''
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
    '''
    L'URL http://localhost:5000/projects est automatiquement redirigée
    vers l'adresse canonique http://localhost:5000/projects/ (avec un slash à la fin)
    '''
    return 'The project page'

@app.route('/about')
def about():
    '''
    L'URL http://localhost:5000/about/ (avec un slash à la fin) conduit à une erreur 404
    car l'adresse canonique n'en contient pas
    '''
    return 'The about page'

#Lancer l'application :
#flask --app hello run

#Lancer l'application avec le mode debug :
#flask --app hello --debug run

#Consulter l'application http://localhost:5000