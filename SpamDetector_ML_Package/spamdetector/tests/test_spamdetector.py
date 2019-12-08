from spamdetector import __version__
from spamdetector import CommentClassifier


def test_version():
    assert __version__ == '0.0.1'


def test_is_spam():
	cc = CommentClassifier()
	cc.text = "please subcribe to our channel"
	result = cc.predict()
	assert result == 'Spam'

def test_is_ham():
	cc = CommentClassifier()
	result = cc.classify('great')
	assert result == 'Non-Spam'
