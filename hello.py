from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Lancer l'application :
#flask --app hello run

#Consulter l'application http://localhost:5000