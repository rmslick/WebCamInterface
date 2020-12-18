# WebCamInterface

WebCamInterface is intended as an image processing education tool for kids but is useful for hackers born in the 20th century as well. WebCamInterface.py is a wrapper class around opencv meant to reduce unsavory details required to perform basic image processing tasks.  

Suggestions welcome.  

NOTE: If any attempt to cite this work is attempted, it will be summarily rejected.  Steal as you will.
## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install opencv and numpy.

```bash
pip install opencv-python
pip install numpy
```

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
[Lol.]
