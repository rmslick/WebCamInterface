from WebCamInterface import *
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