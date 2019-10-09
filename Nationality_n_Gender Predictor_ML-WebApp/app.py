from flask import Flask,render_template,url_for,request
import numpy as np 


# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib


app = Flask(__name__)
# Prediction
def predict_gender(x):
	vect = gender_cv.transform(data).toarray()
	result = gender_clf.predict(vect)
	return result

# Prediction
def predict_nationality(x):
	vect = nationality_cv.transform(data).toarray()
	result = nationality_clf.predict(vect)
	return result




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/gender')
def gender():
	return render_template('gender.html')

@app.route('/predict', methods=['POST'])
def predict():
	# Load Our Count Vectorizer
	nationality_vectorizer = open("models/nationality_vectorizer.pkl","rb")
	cv_nationality = joblib.load(nationality_vectorizer)

	# Loading our ML Model
	nationality_nv_model = open("models/nationality_nv_model.pkl","rb")
	nationality_clf = joblib.load(nationality_nv_model)

	# Receives the input query from form
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]

		vect = cv_nationality.transform(data).toarray()
		result = nationality_clf.predict(vect)
	
	return render_template('index.html',prediction = result ,name = namequery.upper())


@app.route('/predict_gender', methods=['POST'])
def predict_gender():
	# Load Our Count Vectorizer
	gender_vectorizer = open("models/gender_vectorizer.pkl","rb")
	cv_gender = joblib.load(gender_vectorizer)

	# Loading our ML Model
	gender_clf_nv_model = open("models/naivebayesgendermodel.pkl","rb")
	gender_clf = joblib.load(gender_clf_nv_model)

	# Receives the input query from form
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]

		vect = cv_gender.transform(data).toarray()
		result = gender_clf.predict(vect)
	return render_template('gender.html',prediction = result ,name = namequery.upper())


if __name__ == '__main__':
	app.run(debug=True)