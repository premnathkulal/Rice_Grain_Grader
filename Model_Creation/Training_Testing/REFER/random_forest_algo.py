#https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
import pandas as pd
import numpy as np
from sklearn.externals import joblib

dataset = pd.read_csv("test.csv")
X = dataset.iloc[:, 0:6].values
y = dataset.iloc[:, 6].values

for i in range(len(y)):
    if y[i] == 'damage' or y[i] == 0:
        y[i] = 0
    else:
        y[i] = 1

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)

filename = 'random_forest_model.pkl'
joblib.dump(regressor,filename)

y_pred = regressor.predict(X_test)
#X_test
for i in range(len(y_test)):
    print(y_test[i], y_pred[i].round())

# Load model from file
#classifer = joblib.load(filename)
#predicted = classifer.predict([[105.977340698242,146.155487060547,0.725099979683552,11691,73,440.877197146416]])
#print(predicted)