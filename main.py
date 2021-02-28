from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', title='Home page')

@app.route('/home')
def home():
    return 'is home'

@app.route('/help')
def help():
    return 'is help'

app.run()
