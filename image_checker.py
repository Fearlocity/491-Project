# This program will be used to verify that all photos are useable
import os
import cv2
import imghdr

# Change directory to where you are storing your images
data_dir = r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\flowers' 


image_types = ['jpeg','jpg', 'bmp', 'png']

for folders in os.listdir(data_dir): 
    for image in os.listdir(os.path.join(data_dir, folders)):
        image_path = os.path.join(data_dir, folders, image)
        try: 
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_types: 
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e: 
            print('Issue with image {}'.format(image_path))