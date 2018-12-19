from flask import Flask,url_for,request,render_template,jsonify,send_file
from flask_bootstrap import Bootstrap
import json

# NLP Pkgs
import spacy
from textblob import TextBlob 
nlp = spacy.load('en')

# WordCloud & Matplotlib Packages
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from io import BytesIO
import random
import time



# Initialize App
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
	start = time.time()
	# Receives the input query from form
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		# Analysis
		docx = nlp(rawtext)
		# Tokens
		custom_tokens = [token.text for token in docx ]
		# Word Info
		custom_wordinfo = [(token.text,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
		custom_postagging = [(word.text,word.tag_,word.pos_,word.dep_) for word in docx]
		# NER
		custom_namedentities = [(entity.text,entity.label_)for entity in docx.ents]
		blob = TextBlob(rawtext)
		blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity
		# allData = ['Token:{},Tag:{},POS:{},Dependency:{},Lemma:{},Shape:{},Alpha:{},IsStopword:{}'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
		allData = [('"Token":"{}","Tag":"{}","POS":"{}","Dependency":"{}","Lemma":"{}","Shape":"{}","Alpha":"{}","IsStopword":"{}"'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop)) for token in docx ]

		result_json = json.dumps(allData, sort_keys = False, indent = 2)

		end = time.time()
		final_time = end-start
	return render_template('index.html',ctext=rawtext,custom_tokens=custom_tokens,custom_postagging=custom_postagging,custom_namedentities=custom_namedentities,custom_wordinfo=custom_wordinfo,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,final_time=final_time,result_json=result_json)

# API ROUTES
@app.route('/api')
def basic_api():
	return render_template('restfulapidocs.html')

# API FOR TOKENS
@app.route('/api/tokens/<string:mytext>',methods=['GET'])
def api_tokens(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mytokens = [token.text for token in docx ]
	return jsonify(mytext,mytokens)

# API FOR LEMMA
@app.route('/api/lemma/<string:mytext>',methods=['GET'])
def api_lemma(mytext):
	# Analysis
	docx = nlp(mytext.strip())
	# Tokens & Lemma
	mylemma = [('Token:{},Lemma:{}'.format(token.text,token.lemma_))for token in docx ]
	return jsonify(mytext,mylemma)

# API FOR NAMED ENTITY
@app.route('/api/ner/<string:mytext>',methods=['GET'])
def api_ner(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mynamedentities = [(entity.text,entity.label_)for entity in docx.ents]
	return jsonify(mytext,mynamedentities)

# API FOR NAMED ENTITY
@app.route('/api/entities/<string:mytext>',methods=['GET'])
def api_entities(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mynamedentities = [(entity.text,entity.label_)for entity in docx.ents]
	return jsonify(mytext,mynamedentities)


# API FOR SENTIMENT ANALYSIS
@app.route('/api/sentiment/<string:mytext>',methods=['GET'])
def api_sentiment(mytext):
	# Analysis
	blob = TextBlob(mytext)
	mysentiment = [ mytext,blob.words,blob.sentiment ]
	return jsonify(mysentiment)

# API FOR MORE WORD ANALYSIS
@app.route('/api/nlpiffy/<string:mytext>',methods=['GET'])
def nlpifyapi(mytext):

	docx = nlp(mytext.strip())
	allData = ['Token:{},Tag:{},POS:{},Dependency:{},Lemma:{},Shape:{},Alpha:{},IsStopword:{}'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
	
	return jsonify(mytext,allData)
	

# IMAGE WORDCLOUD
@app.route('/images')
def imagescloud():
    return "Enter text into url eg. /fig/yourtext "


@app.route('/images/<mytext>')
def images(mytext):
    return render_template("index.html", title=mytext)

@app.route('/fig/<string:mytext>')
def fig(mytext):
    plt.figure(figsize=(20,10))
    wordcloud = WordCloud(background_color='white', mode = "RGB", width = 2000, height = 1000).generate(mytext)
    plt.imshow(wordcloud)
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)