# fashion-mnist

## Building a neural network to classify images from the Fashion-MNIST dataset

Running main.py gave me the following results:

'' 
    Train on 60000 samples
    Epoch 1/30
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.5319 - accuracy: 0.8120
    Epoch 2/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.4002 - accuracy: 0.8543
    Epoch 3/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.3663 - accuracy: 0.8657
    Epoch 4/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.3444 - accuracy: 0.8739
    Epoch 5/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.3326 - accuracy: 0.8786
    Epoch 6/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.3170 - accuracy: 0.8816
    Epoch 7/30
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.3073 - accuracy: 0.8850
    Epoch 8/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.3005 - accuracy: 0.8892
    Epoch 9/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2896 - accuracy: 0.8923
    Epoch 10/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2843 - accuracy: 0.8945
    Epoch 11/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2739 - accuracy: 0.8975
    Epoch 12/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2704 - accuracy: 0.8981
    Epoch 13/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2657 - accuracy: 0.9002
    Epoch 14/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2619 - accuracy: 0.9027
    Epoch 15/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2565 - accuracy: 0.9042
    Epoch 16/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2528 - accuracy: 0.9044
    Epoch 17/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2472 - accuracy: 0.9060
    Epoch 18/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2430 - accuracy: 0.9085
    Epoch 19/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2400 - accuracy: 0.9100
    Epoch 20/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2370 - accuracy: 0.9100
    Epoch 21/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2325 - accuracy: 0.9120
    Epoch 22/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2313 - accuracy: 0.9125
    Epoch 23/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2236 - accuracy: 0.9149
    Epoch 24/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2245 - accuracy: 0.9141
    Epoch 25/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2182 - accuracy: 0.9169
    Epoch 26/30
    60000/60000 [==============================] - 2s 27us/sample - loss: 0.2197 - accuracy: 0.9165
    Epoch 27/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2166 - accuracy: 0.9169
    Epoch 28/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2134 - accuracy: 0.9182
    Epoch 29/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2109 - accuracy: 0.9208
    Epoch 30/30
    60000/60000 [==============================] - 2s 26us/sample - loss: 0.2080 - accuracy: 0.9201
    10000/10000 [==============================] - 0s 20us/sample - loss: 0.3503 - accuracy: 0.8923
    Test accuracy: 0.8923 Test loss: 0.3502905108869076
''
Despite adding a Dropout layer and an EarlyStopping callback, the model still seems to suffer a bit from overfitting