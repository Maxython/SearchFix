from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException
from random import randint
from json import loads, dumps
from parsing import search

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

@app.route('/find/<find_text>/')
def find(find_text):
    a = search(find_text)
    a.all(github=loads(request.args.get('github')),
    number_of_comments=loads(request.args.get('number_of_comments')),
    rtd=loads(request.args.get('rtd')),
    quantity=loads(request.args.get('quantity')),
    habr=loads(request.args.get('habr')),
    total=loads(request.args.get('total')),
    hqna=loads(request.args.get('hqna')),
    answer=loads(request.args.get('answer')),
    quantity_answer=loads(request.args.get('quantity_answer')))
    return render_template('find.html', title=find_text.replace('+', ' '), find_text=find_text, result=a.result)

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/api/<find_text>/')
def api_find(find_text):
    a = search(find_text)
    github=request.args.get('github')
    rtd=request.args.get('rtd')
    habr=request.args.get('habr')
    hqna=request.args.get('hqna')
    answer=request.args.get('answer')
    number_of_comments=request.args.get('number_of_comments')
    quantity=request.args.get('quantity')
    total=request.args.get('total')
    quantity_answer=request.args.get('quantity_answer')
    try:
        a.all(github=loads(github if github != None else 'true'),
        number_of_comments=loads(github if github != None else 'null'),
        rtd=loads(rtd if rtd != None else 'true'),
        quantity=loads(github if github != None else 'null'),
        habr=loads(habr if habr != None else 'true'),
        total=loads(github if github != None else 'null'),
        hqna=loads(hqna if hqna != None else 'true'),
        answer=loads(answer if answer != None else 'true'),
        quantity_answer=loads(github if github != None else 'null'))
        return dumps(a.result)
    except TypeError:
        return dumps({'error': 500})

@app.errorhandler(Exception)
def error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return render_template('error.html', error=code, url=f'/static/img/siba{randint(1, 4) if randint(1, 10) == 1 else randint(1, 3)}.jpg'), code

app.run()

#https://github.com/search?q={{ TEXT }}&type=issues  GitHub
#https://stackoverflow.com/search?q={{ TEXT }}  StackOverflow
#https://readthedocs.org/projects/docs/search/?q={{ TEXT }}&project=docs Read The Docs
#https://habr.com/en/search/page1/?target_type=posts&order_by=relevance&q={{ TEXT }}&flow= Habr
#https://qna.habr.com/search/questions?q={{ TEXT }}&page=1 Habrqna
