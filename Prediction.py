from utils import *
import cv2
#import matplotlib.pyplot as plt

#predicting
filepath="C:/Indoor Scene Recognition/"

def prepare(img):
    #preprocessing the new image
    img_array = cv2.imread(filepath+str(img),cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (100,100))
    return new_array.reshape(-1,100,100,1)
    
img_array = cv2.imread("C:/Indoor Scene Recognition/airport_inside_0030.jpg",cv2.IMREAD_GRAYSCALE)
new_array = cv2.resize(img_array, (100,100))
new_array=new_array.reshape(-1,100,100,1)
prediction = model.predict([new_array])
print(categories[np.argmax(prediction)])
img="airport1.jpg"