from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    #pour éviter l'injection de code malveillant en exécutant un url de ce type : http://localhost:5000/<script>alert("bad")</script>
    return f"<p>Hello, {escape(name)}</p>"