"""Models to predict purchase intention and Lifetime Value"""
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import OneHotEncoder



df = pd.read_excel(io='dataset.xlsx', sheet_name='Dataset_', usecols='A:M')
df.info

LTV = pd.read_excel(io='dataset.xlsx', sheet_name='LTV_Usuarios', usecols='A:B')
LTV.info

df = pd.merge(df, LTV, how = 'left', on='Id')
df['LTV'].fillna(0, inplace=True)
df.info
df.dtypes
df.head()

###### Purchase intention ######

#### Preprocesing data
# Encoding categorical values
labelecoder = preprocessing.LabelEncoder()
df['mail'] = labelecoder.fit_transform(df['Dominio Correo'])
df['chanel'] = labelecoder.fit_transform(df['Canal Adquisicion'])
df['location'] = labelecoder.fit_transform(df['Ubicación'])

pd.Categorical(df[['Contacto Inicial', 'Reportes Descargados', 'Persona Juridica', 'Interes de Compra']])
df.dtypes
df.info()

# Selectin variables
X = np.asarray(df[['mail', 'chanel', 'location', 'Facturas Creadas', 'Cotizaciones creadas',
	'Contacto Inicial', 'Visitas Blog', 'Reportes Descargados',
	'Persona Juridica', 'Solicita Ayuda']])
y = np.asarray(df['Interes de Compra'])

# Getting training and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Logistic Classifier
clf = LogisticRegression(random_state=0)
clf.fit(X_train, y_train)
score= clf.score(X_test, y_test)
score
clf.predict(X_test)
clf.predict_proba(X_test)

def plot_confusion(clf, X_test, y_test):
	np.set_printoptions(precision=2)
	class_names = ['Compró', 'No Compró']
	# Plot non-normalized confusion matrix
	titles_options = [("Confusion matrix, without normalization", None),
					("Normalized confusion matrix", 'true')]
	for title, normalize in titles_options:
		disp = plot_confusion_matrix(clf, X_test,
									y_test,
									display_labels=class_names,
									cmap=plt.cm.Blues,
									normalize=normalize)
		disp.ax_.set_title(title)
		print(title)
		print(disp.confusion_matrix)
	plt.show()

plot_confusion(clf, X_test, y_test)

# Support Vector Machine classifier
clf = SVC(gamma='auto', random_state=0)
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
score
plot_confusion(clf, X_test, y_test)


##### Lifetime Value ####

# Filter data base
df1 = df[df['Interes de Compra']==1]

df1 = df1[['Dominio Correo', 'Canal Adquisicion', 'Ubicación', 'Facturas Creadas', 'Cotizaciones creadas', 'Contacto Inicial', 'Visitas Blog', 'Reportes Descargados', 'Persona Juridica', 'Solicita Ayuda','LTV']]

df1 = pd.get_dummies(df1, columns=['Dominio Correo', 'Canal Adquisicion', 'Ubicación'])
df1.info()

# Checking correlation between variables
corrMatrix = df1.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()

## Regression Model

X = df1.drop(columns='LTV')
X = X.drop(columns='Canal Adquisicion_Canal Tradicional')
y = df1['LTV']
reg = LinearRegression().fit(X, y)
reg.score(X, y)

np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})

reg.coef_
reg.intercept_
cdf = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(reg.coef_))], axis = 1)
print(cdf)

## SVM Regression Model
reg = SVR(kernel='linear').fit(X, y)
reg.score(X, y)
reg.coef_
reg.intercept_
cdf = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(reg.coef_))], axis = 1)
print(cdf)

# transforming variable to Logaritm
df1['lnLTV'] = np.log(df1['LTV'])

y = df1['lnLTV']

## Regression Model
reg = LinearRegression().fit(X, y)
reg.score(X, y)
reg.coef_
reg.intercept_
cdf = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(reg.coef_))], axis = 1)
print(cdf)
