import sys, os, time, json, hashlib
import datetime as dt
from flask import Flask, render_template, session, request, redirect, url_for
from flask import make_response
from functools import wraps, update_wrapper

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

app.secret_key = os.urandom(12) #generate secret key
if __name__ == "__main__":
    app.run(debug=True) #run Flask application
