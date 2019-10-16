from flask import Flask,render_template,url_for,request,jsonify

# ML Pkg
from sklearn.externals import joblib
# load Vectorizer For Gender Prediction
gender_vectorizer = open("models/gender_vectorizer.pkl","rb")
gender_cv = joblib.load(gender_vectorizer)

# load Model For Gender Prediction
gender_nv_model = open("models/naivebayesgendermodel.pkl","rb")
gender_clf = joblib.load(gender_nv_model)


# Load Vectorizer For Nationality Prediction
nationality_vectorizer = open("models/nationality_vectorizer.pkl","rb")
nationality_cv = joblib.load(nationality_vectorizer)
# Load Models For Nationality Prediction
nationality_nv_model = open("models/nationality_nv_model.pkl","rb")
nationality_clf = joblib.load(nationality_nv_model)


# Init App
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/gender')
def gender():
	return render_template('gender.html')


@app.route('/api')
def api():
	return render_template('api_docs.html')


# ML Routes
@app.route('/predict',methods=['GET','POST'])
def predict():
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]

		# ML
		vect = nationality_cv.transform(data).toarray()
		result = nationality_clf.predict(vect)

	return render_template('index.html',name=namequery.upper(),prediction=result)


@app.route('/predict_gender',methods=['GET','POST'])
def predict_gender():
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]

		# ML
		vect = gender_cv.transform(data).toarray()
		result = gender_clf.predict(vect)
	return render_template('gender.html',name=namequery.title(),prediction=result)


# Api
@app.route('/api/nationality/<string:name>')
def api_nationality(name):
	data = [name]

		# ML
	vect = nationality_cv.transform(data).toarray()
	result = nationality_clf.predict(vect)

	return jsonify({"original name":name,"prediction":result[0]})


@app.route('/api/gender/<string:name>')
def api_gender(name):
	data= [name]

		# ML
	vect = gender_cv.transform(data).toarray()
	cus_prediction = gender_clf.predict(vect)
	if cus_prediction == 0:
		result = 'Female'
	else:
		result = 'Male'

	return jsonify({"original name":name,"prediction":result})

if __name__ == '__main__':
	app.run(debug=True)