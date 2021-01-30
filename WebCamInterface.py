import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def GetFrame():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    colorFrame = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    return colorFrame
def ShowFrame(frame):
    cv2.imshow('frame',frame)
# Simple function to close windows if 'q' is pressed
def CheckQuit():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    else:
        return False 
def CleanUp():  
    cap.release()
    cv2.destroyAllWindows()

# Function to add title to top left
def AddFrameTitle(text, frame):
    # describe the type of font 
    # to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # Use putText() method for 
    # inserting text on video 
    cv2.putText(frame,  
                text,  
                (50, 50),  
                font, 1,  
                (0, 255, 0),  
                2,  
                cv2.LINE_4)
    return frame
def SaveFrame(name,frame):
    cv2.imwrite(name, frame) 
'''
while True:
    # Capture frame from VC
    colorFrame = GetFrame()
    # Add frame title
    colorFrame = AddFrameTitle("Security Feed", colorFrame)
    # Display frame to window
    ShowFrame(colorFrame)
    # Check to see if quit
    if CheckQuit():
        break

CleanUp()
'''