from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
	return '<h1>Welcome to home </h1>'
def create_app():
	app.config['SECRET_KEY'] = "jshiihhheii"
	return app
