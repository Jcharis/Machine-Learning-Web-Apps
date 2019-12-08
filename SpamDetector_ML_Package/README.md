### Using Machine Learning Models as a Package

#### Spamdetector ML Package

#### Resources
+ jupyter notebook with how the model was built
+ video tutorials
+ Using Poetry to Build Packages


#### Code
```bash
pip install poetry
```

#### Create A New Project and Package
```bash
poetry new spamdetector
```

#### Add Packages to Our Project
```bash
poetry add joblib scikit-learn
```


#### Building the Package

```bash
poetry publish
```
### NB
+ You need to create a TestPyPI and  PyPI account to be able to publish officially
for the general public.


#### Usage of Package

```python
>>> from spamdetector import CommentClassifier
>>> cc = CommentClassifier()
>>> cc.text = "this is a great tutorials"
>>> cc.predict()

```

#### Loading Different Models and Classify
```python
>>> from spamdetector import CommentClassifier
>>> cc = CommentClassifier()
>>> cc.text = "this is a great tutorials"
>>> cc.load('nb')

```

```python
>>> from spamdetector import CommentClassifier
>>> cc = CommentClassifier()
>>> mytext = "this is a great tutorials"
>>> cc.classify(mytext)
```

#### .
+ Jesus Saves@JCharisTech
+ Jesse E.Agbe(JCharis)