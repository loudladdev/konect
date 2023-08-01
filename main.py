from website import create_app

app = create_app()

if _name__ == '__main__':
	app.run(debug = True)
