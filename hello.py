from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import abort

app = Flask(__name__)


@app.route('/unauthorized')
def render_unauthorized_error():
    abort(401)

@app.route('/404')
def render_404_error():
    return render_template('404.html')
