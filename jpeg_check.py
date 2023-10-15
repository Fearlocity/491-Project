import os
import cv2
import imghdr
import numpy

# Change directory to where you are storing your images
data_dir = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\flowers\sunflower' 


for image in os.listdir(data_dir): 
    with open(os.path.join(data_dir, image), 'rb') as f:
        check_chars = f.read()[-2:]
    if check_chars != b'\xff\xd9':
        print('Not complete image' + image)
        temp = os.path.join(data_dir, image)
        os.remove(temp)
    else:
        imrgb = cv2.imread(os.path.join(data_dir, image), 1)