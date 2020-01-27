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

render_image(5) #test image rendering with normalised values

#time to create the model