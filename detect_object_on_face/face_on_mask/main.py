import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

tf.keras.models.load_model(
    './keras_model.h5', custom_objects=None, compile=True, options=None
)


camera = cv2.VideoCapture(0)

labels = open('labels.txt', 'r').readlines()

while True:
    
    ret, image = camera.read()
  
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
   
    cv2.imshow('Webcam Image', image)
    
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
   
    image = (image / 127.5) - 1
  
    probabilities = model.predict(image)

    print(labels[np.argmax(probabilities)])

    keyboard_input = cv2.waitKey(1)
   
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
