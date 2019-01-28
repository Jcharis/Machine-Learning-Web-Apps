from flask import Flask,render_template,request,url_for
import pandas as pd 
import numpy as np 

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

# NLP
from textblob import TextBlob 

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])
def predict():
	df= pd.read_csv("data/kjvmindata.csv")
	# Features and Labels
	df_X = df.text
	df_Y = df.label
    
    # Vectorization
	corpus = df_X
	cv = CountVectorizer()
	X = cv.fit_transform(corpus) 

	naivebayes_model = open("models/biblepredictionNV_model.pkl","rb")
	clf = joblib.load(naivebayes_model)

	if request.method == 'POST':
		raw_text = request.form['rawtext']
		data = [raw_text]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
		pred_score = clf.predict_proba(vect)
		nlp_text = TextBlob(raw_text)
		text_sentiment = nlp_text.sentiment.polarity
		verse_sentiment = text_sentiment

	return render_template('index.html',prediction=my_prediction,pred_score=pred_score,verse_sentiment=verse_sentiment,raw_text=raw_text)


if __name__ == '__main__':
	app.run(debug=True)

		