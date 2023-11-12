from tensorflow.keras.models import load_model

model = load_model(r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\flowers.h5' )
test = model.predict(r'C:\Users\Kelton2\Desktop\school stuff\cpsc 491\491-Project\Image_Analyzer\validation_images\rose.jpg' )
print(test)