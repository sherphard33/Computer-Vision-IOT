# Phoenix magicianGirl 12/04/2018

# import the necessary packages
from __future__ import division
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from gpiozero import LEDBoard #Comment out inorder to test on pc
from gpiozero.tools import random_values #Comment out inorder to test on pc
from imutils.video import VideoStream
from threading import Thread
import RPi.GPIO as GPIO #Comment out inorder to test on pc
import Adafruit_PCA9685 #Comment out inorder to test on pc
from _thread import *
import numpy as np
import requests
import imutils
import socket
import datetime
import random
from gun import * #Comment out inorder to test on pc

import sys
import time
import cv2
import os



def purple_rain(p):
	# construct the command to play the music, then execute the
	# command
	command = "aplay -q {}".format(p)
	os.system(command)

# rest gun.
	gunThread = Thread(target=rest, args=())
	gunThread.daemon = True
	gunThread.start()	

# define the paths to the target Keras deep learning model and
# audio file
MODEL_PATH = "target.model"
AUDIO_PATH = "gun.wav"

# initialize the total number of frames that *consecutively* contain
# target along with threshold required to trigger the gun sound
TOTAL_CONSEC = 0
TOTAL_THRESH = 20

# initialize if the gun sound has been triggered
Foe = False # change the name to match the name used in making model

# load the model
print("[INFO] Loading Data...")
model = load_model(MODEL_PATH)


     

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] Begin Seaching For Target...")
#vs = VideoStream(src=0).start()   #Uncomment if you are using the camera on your PC
vs = VideoStream(usePiCamera=True).start() # UnComment out to use the cammera on your RaspberryPi
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# prepare the image to be classified by our deep learning network
	image = cv2.resize(frame, (28, 28)) #change image size to match the sizes used in training the target.model file 
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# classify the input image and initialize the label and
	# probability of the prediction
	(notFoe, foe) = model.predict(image)[0]
	label = "Not Target"
	proba = notFoe
	

        
	# check to see if target was detected using our convolutional
	# neural network
	if foe > notFoe:
		# update the label and prediction probability
		label = "Target Aquired"
		proba = foe

		# increment the total number of consecutive frames that
		# contain santa
		TOTAL_CONSEC += 1

		# check to see if we should raise the santa alarm
		if not Foe and TOTAL_CONSEC >= TOTAL_THRESH:
			# indicate that target has been found
			Foe = True

			# light up that Joly fat man.
			gunThread = Thread(target=destroy, args=())
			gunThread.daemon = True
			gunThread.start()
			######
			time.sleep(5)

			# play gun sound
			musicThread = Thread(target=purple_rain,
				args=(AUDIO_PATH,))
			musicThread.daemon = False
			musicThread.start()

	# otherwise, reset the total number of consecutive frames and the
	# gun sound
	else:
		TOTAL_CONSEC = 0
		Foe = False

	# build the label and draw it on the frame
	label = "{}: {:.2f}%".format(label, proba * 100)
	frame = cv2.putText(frame, label, (10, 25),
		cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
