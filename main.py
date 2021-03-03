from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', title='Home page', search=True, home=False, help=False)

@app.route('/home')
def home():
    return render_template('index.html', title='Home', search=False, home=True, help=False)

@app.route('/help')
def help():
    return render_template('index.html', title='Help', search=False, home=False, help=True)

app.run()

#https://github.com/search?q={{ TEXT }}&type=issues  GitHub
#https://stackoverflow.com/search?q={{ TEXT }}  StackOverflow
#https://readthedocs.org/search/?q={{ TEXT }} Read The Docs
#https://habr.com/ru/search/?q={{ TEXT }} Habr
