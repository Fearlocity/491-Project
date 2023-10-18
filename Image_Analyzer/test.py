import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import os

#Limit memory usage on GPU
gpus = tf.config.experimental.list_physical_devices('GPU')
print(gpus)
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)

#Load Data

training_data = tf.keras.preprocessing.image_dataset_from_directory('flowers')
np_iterator = training_data.as_numpy_iterator()
image_batch = np_iterator.next()
print("TEST")
len(image_batch)
