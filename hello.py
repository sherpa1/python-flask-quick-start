from http.client import responses
from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)


# @app.errorhandler(404)
#"""
#ce code gère les erreurs 404
#"""
# def not_found_error(error):
#     return render_template('404.html'), 404

@app.errorhandler(404)
def not_found_error_with_headers(error):
    """
    ce code gère les erreurs 404 et ajoute un header http personnalisé
    """
    response=make_response(render_template('404.html'),404)
    response.headers["X-Something"]="This a custom header value"
    return response

