from http.client import responses
from flask import Flask
from flask import render_template
from flask import make_response
from flask import abort

app = Flask(__name__)

users = [
    {"id":1,"firstname":"John","lastname":"Doe"},
    {"id":2,"firstname":"James","lastname":"White"},
]

def get_all():
    return users

def get_one(id=None):
    found=None
    if not id:
        return None
    else:
        for user in users:
            if user.get('id')==id:
                found = user
                break
            
    return found

@app.get("/users/<int:id>")
def read_one(id=None):
    user = get_one(id)
    
    if not user:
        return render_template('user_not_found.html',id=id),404
    else:
        return {
            "id": user.get("id"),
            "firstname": user.get("firstname"),
            "lastname": user.get("firstname"),
        }

@app.get("/users")
def read_all():
    users = get_all()
    return users