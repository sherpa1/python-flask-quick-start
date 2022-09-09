from http.client import responses
from flask import Flask
from flask import render_template
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
from flask import session
from flask import request

app = Flask(__name__)

#définir une clé secrète pour l'application
#afin de sécuriser les sessions
app.secret_key = b'azertyuiop1234567890*+=_'


@app.route('/')
def index():
    if 'username' in session:
        return f'Utilisateur connecté : {session["username"]}'
    else:
        return "Vous n'êtes pas connécté"
    
@app.route('/signin')
def signin():
    if request.method == 'POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    else :
        return '''
        <form method="POST" action="/login">
            <label for="username">Username</label>
            <input type="text" name="username" placeholder="username"/>
            <label for="password">Password</label>
            <input type="password" name="password" placeholder="password"/>
            <input type="submit" value="signin"/>
        </form>
        '''
        
@app.route('/signout')
def signout():
    session.pop('username',None)
    return redirect(url_for('index'))