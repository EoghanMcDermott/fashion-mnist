# fashion-mnist

## Building a neural network to classify images from the Fashion-MNIST dataset

Running main.py gave me the following results:

```
    Train on 60000 samples, validate on 10000 samples
    Epoch 1/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.5688 - accuracy: 0.8014 - val_loss: 0.4441 - val_accuracy: 0.8433
    Epoch 2/50
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.4257 - accuracy: 0.8474 - val_loss: 0.3930 - val_accuracy: 0.8602
    Epoch 3/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.3915 - accuracy: 0.8576 - val_loss: 0.3866 - val_accuracy: 0.8586
    Epoch 4/50
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.3699 - accuracy: 0.8663 - val_loss: 0.3931 - val_accuracy: 0.8562
    Epoch 5/50
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.3572 - accuracy: 0.8695 - val_loss: 0.3764 - val_accuracy: 0.8626
    Epoch 6/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3444 - accuracy: 0.8719 - val_loss: 0.3710 - val_accuracy: 0.8700
    Epoch 7/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.3353 - accuracy: 0.8760 - val_loss: 0.3599 - val_accuracy: 0.8720
    Epoch 8/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3263 - accuracy: 0.8801 - val_loss: 0.3685 - val_accuracy: 0.8698
    Epoch 9/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.3204 - accuracy: 0.8807 - val_loss: 0.3575 - val_accuracy: 0.8734
    Epoch 10/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3150 - accuracy: 0.8834 - val_loss: 0.3549 - val_accuracy: 0.8766
    Epoch 11/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3090 - accuracy: 0.8855 - val_loss: 0.3522 - val_accuracy: 0.8735
    Epoch 12/50
    60000/60000 [==============================] - 2s 29us/sample - loss: 0.3036 - accuracy: 0.8869 - val_loss: 0.3451 - val_accuracy: 0.8754
    Epoch 13/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.2974 - accuracy: 0.8893 - val_loss: 0.3615 - val_accuracy: 0.8744
    Epoch 14/50
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.2948 - accuracy: 0.8912 - val_loss: 0.3566 - val_accuracy: 0.8758
    Epoch 15/50
    60000/60000 [==============================] - 2s 28us/sample - loss: 0.2918 - accuracy: 0.8903 - val_loss: 0.3575 - val_accuracy: 0.8761
    Epoch 16/50
    60000/60000 [==============================] - 2s 31us/sample - loss: 0.2854 - accuracy: 0.8935 - val_loss: 0.3585 - val_accuracy: 0.8782

    Eoghan@DESKTOP-A7CDBMK MINGW64 ~/Visual Code Workspace/Fashion MNIST (master)
    $ C:/Users/eogha/AppData/Local/Programs/Python/Python37/python.exe "c:/Users/eogha/Visual Code Workspace/Fashion MNIST/main.py"
    2020-01-27 15:50:31.677494: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
    2020-01-27 15:50:31.680311: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
    2020-01-27 15:50:33.609062: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
    2020-01-27 15:50:33.612686: E tensorflow/stream_executor/cuda/cuda_driver.cc:351] failed call to cuInit: UNKNOWN ERROR (303)
    2020-01-27 15:50:33.617396: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-A7CDBMK
    2020-01-27 15:50:33.620435: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-A7CDBMK
    2020-01-27 15:50:33.622699: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
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