from flask import Flask

app = Flask(__name__)

def create_app(app):
	app.config['SECRET_KEY'] = "jshiihhheii"
	return app
