# Light up that Jollie fatman

 This is code for deploying an image recognition model trained using Keras onto a raspberrypi 3B controlling a pan-tilt Gun Turret.
 The script uses Opencv to draw bounding boxes around the target and label it, a Gun.wav file is played when the gun has been moved 
from rest position to shoot position.
 You can train your own model and change the image size dimensions to suit your input image size.
 
 ## Required Hardware
 ``` RaspberryPI 3b+, Adafruit PCA9685 16-Channel Servo Driver, 2 SG90 Servos, 3D printer?optional (given you have PAN/TILT KIT FOR SG90 SERVO), plastic pistol/blaster ```
 
 ## Setup 
 - Install the latest Raspian on a >=32Gig memory/SD card, this words well on a RaspberryPi 3B+ or newer. 
 - Install python 3.6, tensorflow 2.0, Keras(if not bundled with Tensorflow).

