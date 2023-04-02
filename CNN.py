import cv2
import glob
import numpy as np
from keras import models    
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing import image



CNN_Model = models.load_model("CNN_Car_detector.model")

def img_predictor():
    path = state.image_path                                                                                                                                                                                                 
    img = image.load_img(path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)

    pred=CNN_Model.predict(img_batch)
    print("Car is not Damaged: "+str(pred[0][0])+", Car is Damaged: "+str(pred[0][1]))
    if pred[0][0]>pred[0][1]:
        return ("The car is not damaged")
    else:
        return ("The car is damaged")
