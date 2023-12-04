from flask import Flask,render_template,request,redirect,session

import api
from db import Database

app=Flask(__name__)

dbo = Database()
app.secret_key = '1234hm'


@app.route('/')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html', message="Registration Successful, Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")
@app.route('/perform_login', methods=['post'])
def perform_login():
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    response=dbo.search(email,password)
    if response:
        session['logged_in'] = True
        return redirect('/profile')
    else:
        return render_template('login.html', message="Incorrect email/password")

@app.route('/profile')
def profile():
    if session.get('logged_in'):
        return render_template('profile.html')
    else:
        return redirect('/')
@app.route('/ner')
def ner():
    return render_template('ner.html')
@app.route('/perform_ner', methods=['post'])
def perforn_ner():
    if session.get('logged_in'):
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)

        return render_template('ner.html', response=response)
    else:
        return redirect('/')

@app.route('/sentiment')
def sentiment():
    return render_template('Sentiment.html')
@app.route('/perform_sentiment', methods=['post'])
def perforn_sentiment():
    if session.get('logged_in'):
        text = request.form.get('sentiment_text')
        response = api.sentiment(text)
        print(response)


        result = f"Negative: {response['sentiment']['negative']}, Neutral: {response['sentiment']['neutral']}, Positive: {response['sentiment']['positive']}"
        return render_template('Sentiment.html', result=result)
    else:
        return redirect('/')

@app.route('/abuse')
def abuse():
    return render_template('abuse.html')
@app.route('/perform_abuse', methods=['post'])
def perforn_abuse():
    if session.get('logged_in'):
        text = request.form.get('abuse_text')
        response = api.abuse(text)
        print(response)
        return render_template('abuse.html', response=response)



    else:
        return redirect('/')

app.run(debug=True)