import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
from matplotlib import pyplot as plt
import os

# Limit memory usage on GPU to prevent errors
gpus = tf.config.experimental.list_physical_devices('GPU')
print(gpus)
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)

# Load Data

training_data = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\flowers' 
validation_data = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\validation_images' 

training_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = training_datagen.flow_from_directory(
  training_data,
  target_size=(150,150),
  class_mode='categorical'
)



model = Sequential()
# First Convolution
model.add(Conv2D(64, (3,3), activation='relu', input_shape=(150,150,3)))
model.add(MaxPooling2D(2, 2))
# Second Convolution
model.add(Conv2D(64, (3,3), 1, activation='relu'))
model.add(MaxPooling2D(2, 2))
# Third Convolution
model.add(Conv2D(128, (3,3), 1, activation='relu'))
model.add(MaxPooling2D(2, 2))
# Fourth Convolution
model.add(Conv2D(128, (3,3), 1, activation='relu'))
model.add(MaxPooling2D(2, 2))
# Flatten the results
model.add(Flatten())
# 512 neuron hidden layer
model.add(Dense(512, activation='relu'))
model.add(Dense(2, activation='softmax')) # This will increase as we add more flowers

model.compile(
  loss = 'categorical_crossentropy',
  optimizer='rmsprop',
  metrics=['accuracy'])


model.save("flowers.h5")