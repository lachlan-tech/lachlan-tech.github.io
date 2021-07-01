from flask import Flask, redirect, render_template, request, session, url_for
import time
from time import strftime
import pandas as pd
import numpy

app = Flask(__name__)

@app.route('/')
def page():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("aboutUs.html")

@app.route('/apply')
def apply():
    return render_template("apply.html")

@app.route('/contact')
def contact():
    return render_template("contactUs.html")
    
    
if __name__ == '__main__':
    app.run()