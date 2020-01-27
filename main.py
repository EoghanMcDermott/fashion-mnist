#creating a simple model to classify images from the fashion-mnist dataset

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

label_names = ['T-Shirt', 'Trouser', 'Pullover', 'Dress','Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
#have loaded data and know what label index corresponds to what class label

def render_image(index) : #method to render an image from the dataset
    plt.figure()
    plt.title('Label Index: ' + str(train_labels[index]) + '  ' + label_names[train_labels[index]])
    plt.imshow(train_images[index], cmap='gray') #image is greyscale so use cmap=gray to avoid trying to render in colour
    plt.colorbar()
    plt.show()


#need to normalise data in range 0-1, greyscale images so in range 0-255 at present
train_images = train_images/255.0
test_images = test_images/255.0

#render_image(5) #test image rendering with normalised values

model = tf.keras.Sequential() #time to create the model
model.add(tf.keras.layers.Flatten(input_shape=(28,28))) #flatten 28x28 pixel image into one vector of inputs
model.add(tf.keras.layers.Dense(128, activation='relu')) #128 neuron fully connected layer
model.add(tf.keras.layers.Dropout(0.2)) #add dropout layer to avoid overfitting
model.add(tf.keras.layers.Dense(10, activation='softmax')) #use softmax to determine probability image is of 0-9 classes

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#add a callback to help with overfitting
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=4)

model.fit(
    x=train_images, 
    y=train_labels, 
    epochs=50,
    validation_data=(test_images, test_labels),
    callbacks=[stop_early])