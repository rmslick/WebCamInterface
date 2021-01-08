# WebCamInterface

WebCamInterface is intended as an image processing education tool for kids but is useful for hackers born in the 20th century as well. WebCamInterface.py is a wrapper class around opencv meant to reduce unsavory details required to perform basic image processing tasks.  

Suggestions welcome.  


## Requirements

python 3.8.2

Tested on Ubuntu 20.04

See also [requirements.txt](https://github.com/rmslick/WebCamInterface/blob/master/requirements.txt)


## Usage

```python
webCam = WebCamInterface("HelloWorld.avi") # set up and initialize
frame = webCam.readFrame() #obtain image from webcam
webCam.writeFrame(frame) # Write frame to  video file
webCam.showFrame(frame) # Show frame
wc.CleanUp()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
lol.
