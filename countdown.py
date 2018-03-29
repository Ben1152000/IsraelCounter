import sys, os, time, json, hashlib, subprocess
import datetime as dt
from flask import Flask, render_template, session, request, redirect, url_for
from flask import make_response
from functools import wraps, update_wrapper

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

app.secret_key = os.urandom(12)
if __name__ == "__main__":
    host = str(subprocess.check_output(['ipconfig', 'getifaddr', 'en0']))[2:-3] # change host to equal "localhost" when offline
    app.run(debug=True, use_reloader=False, host=host, port="5000") # change use_reloader to True when running
    
