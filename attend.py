import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import base64

# Initialize the webcam
cap = cv2.VideoCapture(0)

# List to store names
names = []

# Open the attendance file in append mode
fob = open('attendance.txt', 'a+')

# Function to enter data into the attendance file
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = "".join(str(z))  # Fixed the string concatenation
        fob.write(z + '\n')
        return names

print('Reading code ..........')

# Function to check data and mark attendance
def checkData(data):
    data = str(data)
    if data in names:
        print('Already Present')
    else:
        print('\n' + str(len(names) + 1) + '\n' + 'Present done')
        enterData(data)

# Main loop to read frames from the webcam and decode QR codes
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
        break
    cv2.imshow("Frame", frame)
    
    # Break the loop if 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break

# Close the attendance file
fob.close()
