# fashion-mnist

## Building a neural network to classify images from the Fashion-MNIST dataset

Running main.py gave me the following results:

```
    Train on 60000 samples, validate on 10000 samples
    Epoch 1/50
    60000/60000 [==============================] - 2s 33us/sample - loss: 0.5281 - accuracy: 0.8107 - val_loss: 0.4147 - val_accuracy: 0.8490
    Epoch 2/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.4010 - accuracy: 0.8547 - val_loss: 0.3853 - val_accuracy: 0.8610
    Epoch 3/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.3669 - accuracy: 0.8674 - val_loss: 0.3756 - val_accuracy: 0.8633
    Epoch 4/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.3489 - accuracy: 0.8702 - val_loss: 0.3658 - val_accuracy: 0.8673
    Epoch 5/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3316 - accuracy: 0.8774 - val_loss: 0.3652 - val_accuracy: 0.8637
    Epoch 6/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3179 - accuracy: 0.8823 - val_loss: 0.3500 - val_accuracy: 0.8735
    Epoch 7/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.3088 - accuracy: 0.8858 - val_loss: 0.3467 - val_accuracy: 0.8777
    Epoch 8/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.2972 - accuracy: 0.8905 - val_loss: 0.3466 - val_accuracy: 0.8783
    Epoch 9/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.2911 - accuracy: 0.8921 - val_loss: 0.3296 - val_accuracy: 0.8840
    Epoch 10/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.2841 - accuracy: 0.8934 - val_loss: 0.3319 - val_accuracy: 0.8860
    Epoch 11/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.2779 - accuracy: 0.8961 - val_loss: 0.3326 - val_accuracy: 0.8808
    Epoch 12/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.2705 - accuracy: 0.8975 - val_loss: 0.3441 - val_accuracy: 0.8832
    Epoch 13/50
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.2674 - accuracy: 0.8999 - val_loss: 0.3402 - val_accuracy: 0.8828
```

Despite adding a Dropout layer and an EarlyStopping callback, the model still seems to suffer a bit from overfitting