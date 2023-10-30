import tensorflow as tf
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

training_data = tf.keras.preprocessing.image_dataset_from_directory('flowers')
np_iterator = training_data.as_numpy_iterator()
image_batch = np_iterator.next()

# Normalize the data to a min/max of 0-1 instead of 0-255
# as this makes the analyzer more efficient
scaled_batch = image_batch[0] / 255

training_data = training_data.map(lambda x, y: (x/255, y))
batch = training_data.as_numpy_iterator().next()

print(len(training_data))
train_size = int(len(training_data)*.7)
val_size = int(len(training_data)*.2)+1
test_size = int(len(training_data)*.1)+1

train = training_data.take(train_size)
val = training_data.skip(train_size).take(val_size)
test = training_data.skip(train_size+val_size).take(test_size)

print(len(test))