import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import numpy as np 
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head())

#since we are performing computation, we need some integral data, hence using preprocessing to convert non numeric stuff

le = preprocessing.LabelEncoder()
#converting to list
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
clas = le.fit_transform(list(data["class"]))

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))#creates a tuple object
Y = list(clas)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y,test_size = 0.1)

#it's important to use odd integers for k, since there might be an ambiguous case
model = KNeighborsClassifier(n_neighbors = 5)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(x_test)):
	print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
	n = model.kneighbors([x_test[x]], 7, True)	
	print("N : ", n)
