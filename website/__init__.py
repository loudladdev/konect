from flask import Flask,render_template, url_for

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
def create_app():
	app.config['SECRET_KEY'] = "jshiihhheii"
	return app
