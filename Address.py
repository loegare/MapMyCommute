# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 09:50:56 2018

@author: Loegare
"""


from flask import Flask, request, render_template,redirect,url_for,render_template_string
#from flask_login import login_required
import string
import urllib3
import json
import certifi
import gmplot
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

app = Flask(__name__)
application = app
@app.route('/',methods=['GET','POST'])
def home():

    if request.method =='GET':
        return render_template('address.html')
    else:
        address = request.form['address']
        exclude = set(string.punctuation)
        address = ''.join(ch for ch in address if ch not in exclude)
        address=address.replace(' ','+')
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(address)
        r=http.request('GET',url)
        d = json.loads(r.data)
        lat = d['results'][0]['geometry']['location']['lat']
        lng = d['results'][0]['geometry']['location']['lng']
        gmap = gmplot.GoogleMapPlotter(lat,lng, 14)
        top_attraction_lats, top_attraction_lons = zip(*[
                (lat,lng)
                ])
        gmap.scatter(top_attraction_lats, top_attraction_lons, size=40, marker=False)

        gmap.draw("templates/my_map.html")
        return render_template('my_map.html')
        return render_template('address.html')
if __name__ == "__main__":
    app.run()