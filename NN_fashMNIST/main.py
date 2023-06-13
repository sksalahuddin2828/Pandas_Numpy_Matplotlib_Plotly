import tensorflow as tf 
from tensorflow import keras
import matplotlib.pyplot as plt 
import numpy as np 

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#its preferred to have the greyscale values of each pixel in between 0 and 1 intead of 0 and 255
train_images = train_images/255.0
test_images = train_images/255.0
'''
#using pyplot to look at some of the images
plt.imshow(train_images[7], cmap = plt.cm.binary)
plt.show()
'''

'''
	Now lets make a model with 784 input neurons and 10 output neurons along with a 128 neuron hidden layer in between
	Using relu as activation function here and flattening the array for each image
	and then for the connections between hidden layer and the output layer would be
	a softmax function, which brings out the probability between 0 and 1.
'''
model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28,28)),
	keras.layers.Dense(128, activation="relu"),
	keras.layers.Dense(10,activation="softmax")
	])	

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)
'''
(test_loss, test_acc) = model.evaluate(test_images, test_labels)

print("Tested Acc: ", test_acc)
'''

prediction = model.predict(test_images)

for i in range(5):
	plt.grid(False)
	plt.imshow(test_images[i], cmap = plt.cm.binary)
	plt.xlabel("Actual: "+ class_names[test_labels[i]])
	plt.title("Prediction "+ class_names[np.argmax(prediction[i])])
	plt.show()
#print(class_name[np.argmax(prediction[0])])
