from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#Lancer l'application :
#flask --app hello run

#Lancer l'application avec le mode debug :
#flask --app hello --debug run

#Consulter l'application http://localhost:5000