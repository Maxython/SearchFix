from flask import Flask, render_template
from random import randint

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def home_page():
    return render_template('search.html', list=list(range(100)))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.errorhandler(Exception)
def error(error):
    return render_template('error.html', url=f'/static/img/siba{randint(1, 4) if randint(1, 10) == 1 else randint(1, 3)}.jpg')

app.run()

#https://github.com/search?q={{ TEXT }}&type=issues  GitHub
#https://stackoverflow.com/search?q={{ TEXT }}  StackOverflow
#https://readthedocs.org/projects/docs/search/?q={{ TEXT }}&project=docs Read The Docs
#https://habr.com/en/search/page1/?target_type=posts&order_by=relevance&q={{ TEXT }}&flow= Habr
#https://qna.habr.com/search/questions?q={{ TEXT }}&page=1 Habrqna
