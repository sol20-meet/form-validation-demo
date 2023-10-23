from flask import Flask, request, redirect, render_template
from flask import session as login_session
import pyrebase
import random
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/calc')
def calc():
	return render_template('calculator.html')


@app.route('/form'  , methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')


    



if __name__ == '__main__':
	app.run(debug=True)
