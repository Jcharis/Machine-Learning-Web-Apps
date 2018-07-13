from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

# Configuration


import os
import datetime
import time


#EDA Packages
import pandas as pd 
import numpy as np 


# ML Packages







@app.route('/')
def index():
	return render_template('index.html')




if __name__ == '__main__':
	app.run(debug=True)