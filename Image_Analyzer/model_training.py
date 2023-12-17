import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense, Flatten, Dropout
import keras as k
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

training_data = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\training_data' 
validation_data = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\test_data' 

training_datagen = ImageDataGenerator(
      rescale = 1./255,
	    rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

train_generator = training_datagen.flow_from_directory(
  training_data,
  target_size=(224,224),
  class_mode='categorical',
  color_mode='rgb',
)

validation_datagen = ImageDataGenerator(rescale = 1./255)

validation_generator = validation_datagen.flow_from_directory(
	validation_data,
	target_size=(224,224),
	class_mode='categorical',
  color_mode='rgb',
  batch_size=25
)

mobilenet = k.applications.mobilenet_v2.MobileNetV2(weights='imagenet', input_shape=(224,224,3), include_top=False)
mobilenet.trainable = False

model = Sequential([mobilenet])

model.add(GlobalAveragePooling2D())

model.add(Dropout(0.4))
model.add(Dense(256, activation='relu'))

model.add(Dropout(0.3))
model.add(Dense(128, activation='relu'))

model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax')) # This will increase as we add more flowers


model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_generator, epochs=45, steps_per_epoch=25, validation_data = validation_generator, verbose = 1, validation_steps=5)
model.save("flowers.keras")