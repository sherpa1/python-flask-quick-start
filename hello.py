from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Lancer l'application :
#flask --app hello run

#Lancer l'application avec le mode debug :
#flask --app hello --debug run

#Consulter l'application http://localhost:5000