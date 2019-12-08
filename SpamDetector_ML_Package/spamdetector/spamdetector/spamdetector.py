import os,joblib
PACKAGE_DIR = os.path.dirname(__file__)

class CommentClassifier(object):
	"""docstring for CommentClassifier"""
	def __init__(self, text=None):
		super(CommentClassifier, self).__init__()
		self.text = text
		
	def __repr__(self):
		return 'CommentClassifier(text={})'.format(self.text)

	def predict(self):
		"""Predict If It is Spam or Not 
		By Default It uses the Naive Bayes Algorithm
		
		s = CommentClassifier()
		s.text = " "
		s.predict()

		"""
		# load Vectorizer For Spam Prediction
		spam_vectorizer = open(os.path.join(PACKAGE_DIR,"models/spam_vectorizer.pkl"),"rb")
		spam_cv = joblib.load(spam_vectorizer)

		# load Model For Spam Prediction
		spam_detector_nb_model = open(os.path.join(PACKAGE_DIR,"models/spam_detector_nb_model.pkl"),"rb")
		spam_detector_clf = joblib.load(spam_detector_nb_model)
		vectorized_data = spam_cv.transform([self.text]).toarray()
		prediction = spam_detector_clf.predict(vectorized_data)
		if prediction[0] == 0:
			result = 'Non-Spam'
		elif prediction[0] == 1:
			result = 'Spam'
		return result

	def load(self,model_type):
		"""
		Load A Model [nb:naive bayes,logit:logisticRegression]
		g = CommentClassifier()
		g.load('nb')

		"""
		if model_type == 'nb':
			spam_detector_nb_model = open(os.path.join(PACKAGE_DIR,"models/spam_detector_nb_model.pkl"),"rb")
			spam_detector_clf = joblib.load(spam_detector_nb_model)
		elif model_type == 'logit':
			spam_detector_logit_model = open(os.path.join(PACKAGE_DIR,"models/spam_detector_logit_model.pkl"),"rb")
			spam_detector_clf = joblib.load(spam_detector_logit_model)
		elif model_type == 'rf':
			spam_detector_rf_model = open(os.path.join(PACKAGE_DIR,"models/spam_detector_rf_model.pkl"),"rb")
			spam_detector_clf = joblib.load(spam_detector_rf_model)
		else:
			print("Please Select A Model Type [nb:naive bayes ,logit: logisticRegression, rf: Random Forest")

		return spam_detector_clf

	def classify(self,new_text):
		"""
		Classify Comment as Spam or Ham

		s = CommentClassifier()
		s.load('nb')
		s.classify('great package')

		"""
		self.text = new_text
	
		result = self.predict()
		return result


	def is_spam(self,new_text):
		
		self.text = new_text
		result = self.predict()
		return result == 'Spam'



# Jesus Saves@JCharisTech