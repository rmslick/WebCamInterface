from WebCamInterface import WebCamInterface

webCam = WebCamInterface("HelloWorld.avi")
while True:
    frame = webCam.readFrame()
    webCam.writeFrame(frame)
    webCam.showFrame(frame)
    if webCam.userQuit():
        webCam.CleanUp()
        break