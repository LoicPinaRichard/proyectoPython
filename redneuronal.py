import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn import datasets
from keras import layers,models
from keras.datasets import mnist
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
tf.config.run_functions_eagerly(False)
from keras.utils.np_utils import to_categorical
(train_data,train_labels),(test_data,test_labels)=mnist.load_data()

model= models.Sequential()
model.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
model.add(layers.Dense(10,activation='softmax'))

model.compile(optimizer='rmsprop',
                        loss='categorical_crossentropy',
                        metrics='accurracy')
model.summary()

x_train= train_data.reshape((60000,28*28))
x_train=x_train.astype('float32')/255

x_test= test_data.reshape((10000,28*28))
x_test=x_test.astype('float32')/255

y_train=to_categorical(train_labels)
y_test=to_categorical(test_labels)

model.fit(x_train,y_train, epochs=5, batch_size=128)

model.evaluate(x_test,y_test)