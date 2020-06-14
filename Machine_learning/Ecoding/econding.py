#!/usr/bin/env python3
"""Label Ecoding with Titanic data Set Kaggle"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('titanic.csv')
# Subdata set copy from original and drop empty obs
data = df[['Survived', 'Sex', 'Age', 'SibSp', 'Fare', 'Embarked']].copy().dropna()
# Creating encoder

# 1. Label Encoding
labelecoder = preprocessing.LabelEncoder()
data['SexClass'] = labelecoder.fit_transform(data['Sex'])
data['EmbarkedClass'] = labelecoder.fit_transform(data['Embarked'])

# First Ml model
clf = SVC(gamma='auto')

X = np.asarray(data[['SexClass', 'Age', 'SibSp', 'Fare', 'EmbarkedClass']])
y = np.asarray(data['Survived'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
clf.fit(X_train, y_train)

score1= clf.score(X_test, y_test)
score1

# 2. One-Hot Encoding
X_ohe = data[['Survived', 'Sex', 'Age', 'SibSp', 'Fare', 'Embarked']].copy()
X_ohe = pd.get_dummies(X_ohe, columns=['Sex', 'Embarked'])

# Second Ml model
X = np.asarray(X_ohe[['Sex_female', 'Sex_male', 'Age', 'SibSp', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S']])
y = np.asarray(X_ohe['Survived'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
clf.fit(X_train, y_train)

score2= clf.score(X_test, y_test)
score2

scoreChange = score2-score1
scoreChange