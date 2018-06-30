# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 00:07:49 2018

@author: Loegare

Open simple webpage and get user entered day of week and time
"""

from flask import Flask, request, render_template,redirect,url_for
#from flask_login import login_required
import pandas as pd
import numpy as np

app = Flask(__name__)
application = app
@app.route('/',methods=['GET','POST'])
def home():
    print(1)
    if request.method =='GET':
        return render_template('Home.html')
    else:
        time = request.form['DeptTime']
        day = request.form['DoW']
        print(day,time)
        return render_template('Home.html')
if __name__ == "__main__":
    app.run()