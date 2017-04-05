from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from social_flask.routes import social_auth
from social_flask.models import init_social


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(social_auth)

db = SQLAlchemy(app)

init_social(app, session)

@app.route('/')
def hello_world():
        return 'Hello, World!'
