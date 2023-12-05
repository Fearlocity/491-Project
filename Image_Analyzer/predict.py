import tensorflow as tf
from tensorflow.keras.models import load_model
import keras.utils as image
import numpy as np

model_file = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\flowers.keras'
image_file = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\test_data\dandelion\3533075436_0954145b9f_m.jpg'
flowers = ["daisy", "dandelion", "rose", "sunflower", "tulip"]
print("loading model")
image = tf.keras.preprocessing.image.load_img(image_file, target_size=(224, 224))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])
model = tf.keras.models.load_model(filepath = model_file)
print("predicting image")
test = model.predict(input_arr)
iter = 0
highest = 0
prediction = ''
for x in flowers:
    if (test[0][iter]) > highest:
        highest = (test[0][iter])
        prediction = x
    iter+= 1

print("The predicted flower is: ")
print(prediction)