# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:21:01 2018

@author: Hesam
"""

from flask import Flask, session,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
