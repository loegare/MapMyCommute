# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 00:07:49 2018

@author: Loegare

Open simple webpage and get user entered day of week and time
"""

from flask import Flask, request, render_template,redirect,url_for,render_template_string
#from flask_login import login_required
import pandas as pd
import numpy as np
import json
from datetime import datetime,timedelta,timezone

app = Flask(__name__)
application = app
@app.route('/Home',methods=['GET','POST'])
def home():
    curDate = datetime.now(timezone.utc)
    deptDatetime = curDate-timedelta(minutes=curDate.minute)
    deptDatetime = deptDatetime-timedelta(hours=deptDatetime.hour)
    deptDatetime = deptDatetime-timedelta(days=deptDatetime.weekday())
    deptDatetime = deptDatetime+timedelta(days=7)
    if request.method =='GET':
        return render_template('Home.html')
    else:
        time = request.form['DeptTime']
        print(time)
        day = request.form['DoW']
        print(day)
#        tzOffset = request.form['test']
        data = request.get_json()
        print(data)
#        deptDatetime = deptDatetime + timedelta(days=day)
#        deptDatetime = deptDatetime + timedelta(hours=time)
#        print(tzOffset)
        return render_template('Home.html')
    

if __name__ == "__main__":
    app.run()