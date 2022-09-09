from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)


def valid_login(username,password):
    if not username or not password:
        return False
    elif username == "john@doe.com" and password=="Azerty":
        return True
    else:
        return False

def log_the_user_in(username):
    return f"<p>Welcome {username}</p>"

@app.route('/')
def redirect_to_login():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():    
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

#Lancer l'application :
#flask --app hello run

#Lancer l'application avec le mode debug :
#flask --app hello --debug run

#Consulter l'application http://localhost:5000/login