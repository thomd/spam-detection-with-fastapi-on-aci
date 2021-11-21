import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from joblib import dump
import texthelper as th


dataset = pd.read_csv("./data/spam.csv")
X = dataset["Message"].apply(th.preprocessor)
y = dataset["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


vectorizer = TfidfVectorizer(strip_accents=None, lowercase=False, max_features=700, ngram_range=(1, 1))
pipeline = Pipeline([("vectorizer", vectorizer), ("nn", MLPClassifier(hidden_layer_sizes=(700, 700)))])
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print(f"Accuracy: {100 * accuracy_score(y_test, y_pred)} %")

dump(pipeline, "./model/spam-classifier.joblib")
