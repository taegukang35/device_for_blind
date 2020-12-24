import cv2
import os
cam_directory = " "
store_foldee_directory = ""
cam = cv2.VideoCapture(cam_directory)
currentframe = 0

while(True):
    ret, frame = cam.read()
    if ret:
        name = store_foldee_directory + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name,frame)
        currentframe += 1
    else
        break
cam.realease()
cv2.destroyWindow()