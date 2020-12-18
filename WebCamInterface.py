import numpy as np
import os
import cv2

# Wrapper class to reduce function calls and interaction
# with opencv image tools.

# Meant for hackers, kids and cool people in general.

class WebCamInterface:
    def __init__(self, filename = 'video.avi'):
        self.filename = filename
        self.frames_per_second = 24.0
        self.res = '720p'
        self.STD_DIMENSIONS =  {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }
        self.VIDEO_TYPE = {'avi': cv2.VideoWriter_fourcc(*'XVID'),'mp4': cv2.VideoWriter_fourcc(*'XVID')}
        self.cap = cv2.VideoCapture(0)
        self.out = self.InitializeVideoWriter()
    # Camera settings below
    def change_res(self, width, height):
        self.cap.set(3, width)
        self.cap.set(4, height)
    def get_dims(self, res='1080p'):
        width, height = self.STD_DIMENSIONS["480p"]
        if self.res in self.STD_DIMENSIONS:
            width,height = self.STD_DIMENSIONS[self.res]
        self.change_res(width, height)
        return width, height
    def get_video_type(self):
        self.filename, ext = os.path.splitext(self.filename)
        if ext in self.VIDEO_TYPE:
            return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']

    def InitializeVideoWriter(self):
        return cv2.VideoWriter(self.filename, self.get_video_type(), 25, self.get_dims( self.res))
    # Fun stuff below
    def readFrame(self):
        ret, frame = self.cap.read()
        return frame
    # Will use frame that was passed in to constructor
    def writeFrame(self, frame):
        self.out.write(frame)
    def showFrame(self, frame):
        cv2.imshow('frame',frame)
    def userQuit(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return True
        else:
            return False
    def CleanUp(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
    def WriteOnFrame(self, frame, text):
        # describe the type of font 
        # to be used. 
        font = cv2.FONT_HERSHEY_SIMPLEX 
    
        # Use putText() method for 
        # inserting text on video 
        cv2.putText(frame,  
                    text,  
                    (50, 50),  
                    font, 1,  
                    (0, 255, 255),  
                    2,  
                    cv2.LINE_4) 
        return frame
#webCam = WebCamInterface("HelloWorld.avi")
#while True:
#    frame = webCam.readFrame()
#    webCam.writeFrame(frame)
#    webCam.showFrame(frame)
#    if webCam.userQuit():
#        break