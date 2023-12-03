import tensorflow as tf
from tensorflow.keras.models import load_model
import keras.utils as image
import numpy as np

model_file = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\flowers.keras'
image_file = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\test_data\rose\Image_5.jpg'
print("loading model")
image = tf.keras.preprocessing.image.load_img(image_file, target_size=(224, 224))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])
model = tf.keras.models.load_model(filepath = model_file)
print("predicting image")
test = model.predict(input_arr)
print(test)