'''
sudo apt-get install libasound2-dev libasound2 libasound2-plugins
sudo apt-get install python-dev
sudo pipenv install pyaudio
sudo apt-get install libportaudio-dev
sudo apt-get install portaudio19-dev
pip install pyaudio in environment. sudo apt-get install pyaudio

sudo apt-get install numpy

sudo apt-get install libjpeg9-dev
pip install pillow
pip3 install virtualenv --user  !!!!!!! got to be in the user not the global
pip3 install opencv-python

Raspbian Stretch includes configuration for pip to use piwheels by default. If you're using an alternate distribution (or an older version of Raspbian), you can use piwheels by placing the following lines in /etc/pip.conf:

[global]
extra-index-url=https://www.piwheels.org/simple

pip install opencv-python
https://blog.piwheels.org/new-opencv-builds/

pi@spypi:~/spiPi $ sudo apt-get install libatlas3-base libwebp5
Reading package lists... Done
Building dependency tree
Reading state information... Done
libwebp5 is already the newest version.
libwebp5 set to manually installed.
The following package was automatically installed and is no longer required:
  libportaudio0
Use 'apt-get autoremove' to remove it.
The following NEW packages will be installed:
  libatlas3-base
0 upgraded, 1 newly installed, 0 to remove and 162 not upgraded.
Need to get 1,841 kB of archives.
After this operation, 8,229 kB of additional disk space will be used.
https://blog.piwheels.org/new-opencv-builds/
https://blog.piwheels.org/new-opencv-builds/
https://blog.piwheels.org/new-opencv-builds/

https://blog.piwheels.org/new-opencv-builds/https://blog.piwheels.org/new-opencv-builds/https://blog.piwheels.org/new-opencv-builds/https://blog.piwheels.org/new-opencv-builds/

sudo apt-get install libatlas3-base libwebp5 libtiff5 libjasper1 libilmbase6 libopenexr6  libgstreamer1.0-0 libavcodec56 libavformat libavutil54 libswscale3 libqtgui4 libqt4-test libqtcore4
libavformat56    libavformat-dev
(venv) pi@spypi:~/spiPi $ sudo apt-get install libatlas3-base libwebp5 libtiff5 libjasper1 libilmbase6 libopenexr6  libgstreamer1.0-0 libavcodec56 libavformat56 libavutil libswscale3 libqtgui4 libqt4-test libqtcore4
libavutil54    libavutil-dev
(venv) pi@spypi:~/spiPi $ sudo apt-get install libatlas3-base libwebp5 libtiff5 libjasper1 libilmbase6 libopenexr6  libgstreamer1.0-0 libavcodec libavformat56 libavutil54 libswscale3 libqtgui4 libqt4-test libqtcore4
libavcodec56         libavcodec-dev       libavcodec-extra     libavcodec-extra-56
(venv) pi@spypi:~/spiPi $ sudo apt-get install libatlas3-base libwebp5 libtiff5 libjasper1 libilmbase6 libopenexr6  libgstreamer1.0-0 libavcodec56 libavformat56 libavutil54 libswscale libqtgui4 libqt4-test libqtcore4
libswscale3     libswscale-dev
(venv) pi@spypi:~/spiPi $ sudo apt-get install libatlas3-base libwebp5 libtiff5 libjasper1 libilmbase6 libopenexr6  libgstreamer1.0-0 libavcodec56 libavformat56 libavutil54 libswscale3 libqtgui4 libqt4-test libqtcore4
Reading package lists... Done
Building dependency tree
Reading state information... Done
libatlas3-base is already the newest version.
libgstreamer1.0-0 is already the newest version.
libgstreamer1.0-0 set to manually installed.
libilmbase6 is already the newest version.
libilmbase6 set to manually installed.
libopenexr6 is already the newest version.
libopenexr6 set to manually installed.
libqtcore4 is already the newest version.
libqtcore4 set to manually installed.
libqtgui4 is already the newest version.
libqtgui4 set to manually installed.
libwebp5 is already the newest version.
The following package was automatically installed and is no longer required:
  libportaudio0
Use 'apt-get autoremove' to remove it.
Suggested packages:
  libjasper-runtime
The following NEW packages will be installed:
  libqt4-test
The following packages will be upgraded:
  libavcodec56 libavformat56 libavutil54 libjasper1 libswscale3 libtiff5
6 upgraded, 1 newly installed, 0 to remove and 156 not upgraded.
Need to get 5,681 kB/6,087 kB of archives.
After this operation, 236 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrordirector.raspbian.org/raspbian/ jessie/main libavutil54 armhf 6:11.12-1~deb8u5+rpi1 [164 kB]
Get:2 http://mirrordirector.raspbian.org/raspbian/ jessie/main libavcodec56 armhf 6:11.12-1~deb8u5+rpi1 [4,497 kB]
Get:3 http://mirrordirector.raspbian.org/raspbian/ jessie/main libavformat56 armhf 6:11.12-1~deb8u5+rpi1 [859 kB]
Get:4 http://mirrordirector.raspbian.org/raspbian/ jessie/main libswscale3 armhf 6:11.12-1~deb8u5+rpi1 [160 kB]
Fetched 5,681 kB in 5s (1,065 kB/s)
(Reading database ... 78188 files and directories currently installed.)
Preparing to unpack .../libavutil54_6%3a11.12-1~deb8u5+rpi1_armhf.deb ...
Unpacking libavutil54:armhf (6:11.12-1~deb8u5+rpi1) over (6:11.11-1~deb8u1+rpi1) ...
Preparing to unpack .../libavcodec56_6%3a11.12-1~deb8u5+rpi1_armhf.deb ...
Unpacking libavcodec56:armhf (6:11.12-1~deb8u5+rpi1) over (6:11.11-1~deb8u1+rpi1) ...
Preparing to unpack .../libavformat56_6%3a11.12-1~deb8u5+rpi1_armhf.deb ...
Unpacking libavformat56:armhf (6:11.12-1~deb8u5+rpi1) over (6:11.11-1~deb8u1+rpi1) ...
Preparing to unpack .../libjasper1_1.900.1-debian1-2.4+deb8u5_armhf.deb ...
Unpacking libjasper1:armhf (1.900.1-debian1-2.4+deb8u5) over (1.900.1-debian1-2.4+deb8u3) ...
Selecting previously unselected package libqt4-test:armhf.
Preparing to unpack .../libqt4-test_4%3a4.8.6+git64-g5dc8b2b+dfsg-3+deb8u1+rpi1_armhf.deb ...
Unpacking libqt4-test:armhf (4:4.8.6+git64-g5dc8b2b+dfsg-3+deb8u1+rpi1) ...
Preparing to unpack .../libswscale3_6%3a11.12-1~deb8u5+rpi1_armhf.deb ...
Unpacking libswscale3:armhf (6:11.12-1~deb8u5+rpi1) over (6:11.11-1~deb8u1+rpi1) ...
Preparing to unpack .../libtiff5_4.0.3-12.3+deb8u7_armhf.deb ...
Unpacking libtiff5:armhf (4.0.3-12.3+deb8u7) over (4.0.3-12.3+deb8u5) ...
Setting up libavutil54:armhf (6:11.12-1~deb8u5+rpi1) ...
Setting up libavcodec56:armhf (6:11.12-1~deb8u5+rpi1) ...
Setting up libavformat56:armhf (6:11.12-1~deb8u5+rpi1) ...
Setting up libjasper1:armhf (1.900.1-debian1-2.4+deb8u5) ...
Setting up libqt4-test:armhf (4:4.8.6+git64-g5dc8b2b+dfsg-3+deb8u1+rpi1) ...
Setting up libswscale3:armhf (6:11.12-1~deb8u5+rpi1) ...
Setting up libtiff5:armhf (4.0.3-12.3+deb8u7) ...
Processing triggers for libc-bin (2.19-18+deb8u10) ...


https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/
'''

import io
try:
    import picamera
except ImportError:
    is_picamera = True
import logging

LOG_FILENAME = 'logging.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
import os.path, time
import sys
import socketserver
from threading import Condition
import http.server as server
import os
from PIL import Image
from PIL import ImageChops
import numpy
import cv2
import imutils
import imgencode_proc 
import json
import play_sound as ps
import imgprocessing_proc

# This program has attribution to https://github.com/alexadam/img-encode
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
effect_no = 0
x = 0
y = 0
w = 1 
h = 1
camera = ''

# CAMERA RESOLUTION
width =  20
height = 20
width = int(1366/4)
height = int(768/4)
frameDiffCount = 0
play_sound = ps.play_sound()
image_encoder = imgencode_proc.encoder()
image_processor = imgprocessing_proc.processor()
global encodeImage
encodeImage = False
area = (0,0,width,height)
triggerPixelBox = [0,0,5,5]
diffThresh = 40000
diffRate = 80

ampThresh = 200
class StreamingHandler(server.BaseHTTPRequestHandler):
    global camera, output,x,y,width,height,effect_no,frame,area, encodeImage, frameDiffCount, diffThresh
    def do_GET(self):
        global x,y,width,height,effect_no,frame,area,frameDiffCount
        serverPath = os.path.dirname(os.path.realpath(__file__))
	#logging.info('spyPi API CALL: '+self.path)
        if self.path == '/':
            self.path = '/index.html'
        elif 'chngCoor' in self.path:
            self.send_response(200)
            self.send_header('Location', '/index.html')
            self.end_headers()
            newCrd = list(map(float,self.path.split('?')[1].split(',')))
            crop = ((newCrd[0]/400), (newCrd[1]/400), (newCrd[2]/400), (newCrd[3]/400))
            camera.crop = crop
        elif 'imageSize' in self.path:
            PAGE = '["'+str(height)+'","'+ str(width) + '"]'
            PAGE = json.loads(PAGE)
            content = str(PAGE).encode('utf')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.send_header('Content-Length', len(content))
            self.wfile.write(content)
        elif 'encodeImage' in self.path:
            self.send_response(200)
            self.end_headers()
            if encodeImage==False:
                encodeImage = True
            else:
                encodeImage=False
        elif 'rotate' in self.path:
            if self.path.split('?')[1] == 'right':
                camera.rotation = camera.rotation + 90
            else:
                camera.rotation = camera.rotation - 90
        elif 'shiftUp' in self.path:
            if camera.crop[1] - .015 < 1:
                camera.crop = (camera.crop[0], camera.crop[1] - .015, camera.crop[2],camera.crop[3])
        elif 'shiftDown' in self.path:
            if camera.crop[1] + .015 > 0:
                camera.crop = (camera.crop[0], camera.crop[1] + .015, camera.crop[2],camera.crop[3])
        elif 'shiftLeft' in self.path:
            if camera.crop[0] - .015 < 1:
                camera.crop = (camera.crop[0] - .015, camera.crop[1], camera.crop[2],camera.crop[3])
        elif 'shiftRight' in self.path:
            if camera.crop[0] + .015 > 0:
                camera.crop = (camera.crop[0] + .015, camera.crop[1], camera.crop[2],camera.crop[3])
        elif 'zoomIn' in self.path:
            camera.crop = (camera.crop[0] + .05, camera.crop[1]+.05, camera.crop[2]-.1,camera.crop[3]-.1)
        elif 'zoomOut' in self.path:
            camera.crop = (camera.crop[0] - .05, camera.crop[1]-.05, camera.crop[2]+.1,camera.crop[3]+.1)
        elif 'sharpness' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'contrast' in self.path:
            camera.contrast =  int(self.path.split('?')[1])
        elif 'brightness' in self.path:            
            camera.brightness = int(self.path.split('?')[1])
        elif 'diffThresh' in self.path:            
            diffThresh = int(self.path.split('?')[1])
        elif 'ampThresh' in self.path:            
            ampThresh = int(self.path.split('?')[1])
        elif 'diffRate' in self.path:            
            diffRate = int(self.path.split('?')[1])


        elif 'saturation' in self.path:            
            camera.saturation = int(self.path.split('?')[1])
        elif 'iso' in self.path:            
            camera.ISO = int(self.path.split('?')[1]) 
        elif 'video_stabilization' in self.path:
            camera.video_stabilization = False

            #camera.exposure_compensation = 0
            #camera.exposure_mode = 'auto'
            #camera.meter_mode = 'average'
            #camera.awb_mode = 'auto'
        elif 'image_effect' in self.path:
            #keys = list(camera.IMAGE_EFFECTS.keys())
            camera.image_effect =  self.path.split('?')[1]
        elif 'color_effects' in self.path:            
            camera.color_effects = None
        elif 'hFlip' in self.path:
            if camera.hflip == False:
                camera.hflip = True
            else:
                camera.hflip = False
        elif 'vFlip' in self.path:            
            if camera.vflip == False:
                camera.vflip = True
            else:
                camera.vflip = False

        if self.path == '/index.html':
            
           
            PAGE = open(serverPath + '/bideo.html','r').read()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            s = 0
            frame2xList = []
            frame2yList = []
            frame3xList = []
            frame3yList = []
            x_buffered = []
            x_max = 0
            firstFrame = None
            if True: #True: #checking for frame difference is turned on
                #try:
                while True:
                    if False:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        if False:  
                            print('here')
                            #imgBytes = io.BytesIO(frame)
                            #frame.save(imgBytes, 'BMP')
                            imgBytes = io.BytesIO()
                            frame.save(imgBytes, 'BMP')
                            frame = imgBytes.getvalue()

                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                        
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')
                    
                            
                            '''
                            frame = frame2.convert('RGB')
                            frame = numpy.array(frame)
                            
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            gray = cv2.GaussianBlur(gray, (21, 21), 0)
                     
                            # if the first frame is None, initialize it
                            if firstFrame is None:
                                firstFrame = gray
                                continue
                            # compute the absolute difference between the current frame and
                            # first frame
                            frameDelta = cv2.absdiff(firstFrame, gray)
                            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                     
                            # dilate the thresholded image to fill in holes, then find contours
                            # on thresholded image
                            thresh = cv2.dilate(thresh, None, iterations=2)

                            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                            cnts = imutils.grab_contours(cnts)
                     
                            # loop over the contours

                            for c in cnts:
                                    # if the contour is too small, ignore it
                                    if cv2.contourArea(c) < 95:
                                            continue
                     
                                    # compute the bounding box for the contour, draw it on the frame,
                                    # and update the text
                                    (x, y, w, h) = cv2.boundingRect(c)
                                    cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    text = "Occupied"                            
                                                
                            #frame1xList = get_avg_x(frame2Array, 200)
                            #frame.save(serverPath + '/output/current_pic.jpg')
                            '''
                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame2))
                            self.end_headers()
                        
                            self.wfile.write(frame2)
                            self.wfile.write(b'\r\n')
                        '''                                      
                        elif False:
                            frame3 = (Image.open(io.BytesIO(frame))).convert('L')
                            frame3.save(serverPath + '/output/current_pic2.jpg')
                            frameDiffCount = 0
                            frame = ImageChops.difference(frame2, frame3)
                            #frame = frame3
                            #width, height = absDiff.size
                            #frame = frame.convert('RGB')
                            imgBytes = io.BytesIO()
                            frame.save(imgBytes, 'BMP')
                            frame = imgBytes.getvalue()
                            frameDiffCount = 0
                            #s = 0
                            #for x in range(width):
                            #    for y in range(height):
                            #        r, g, b = rgb_im.getpixel((x, y))
                            #        s = r + g + b + s


                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                        
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')
                    
                    if False:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        self.wfile.write(b'--FRAME\r\n')
                        self.send_header('Content-Type', 'image/jpeg')
                        self.send_header('Content-Length', len(frame))
                        self.end_headers()
                        self.wfile.write(frame)
                        self.wfile.write(b'\r\n')
                        if encodeImage:
                            print("image")
                            if frameDiffCount == 0:  
                                frame2 = Image.open(io.BytesIO(frame))
                                frame2.save(serverPath + '/output/current_pic.jpg')
                            elif frameDiffCount == diffRate:
                                print("calculating frame diff")
                                frame3 = Image.open(io.BytesIO(frame))
                                frame3.save(serverPath + '/output/current_pic2.jpg')
                                frameDiffCount = 0
                                absDiff = ImageChops.difference(frame2, frame3)
                                width, height = absDiff.size
                                rgb_im = absDiff.convert('RGB')
                                s = 0
                                for x in range(width):
                                    for y in range(height):
                                        r, g, b = rgb_im.getpixel((x, y))
                                        s = r + g + b + s

                            frameDiffCount += 1

                            if s > diffThresh and encodeImage:
                                print('ecoding due to frame diffe frame diff / threshold: ',s ,' / ',diffThresh , '= ', s  / diffThresh) 
                                s = 0
                                #encodeImage = False
                                frame2 = Image.open(io.BytesIO(frame))
                                frame2.save(serverPath + '/output/current_pic.jpg')
                                
                                #modifiedTime = time.ctime(os.path.getmtime('./output/current_pic.wav'))
                                #createdTime = time.ctime(os.path.getctime('./output/current_pic.wav'))
                                 
                                #encodedOutput = 
                                image_encoder.encodeObject(serverPath + '/output/current_pic.jpg', './output/current_pic.wav','.75' )
                                #print(encodedOutput)
                                #stdoutdata, stderrdata = encodedOutput.communicate()
                                #print(stdoutdata)
                                #print(stderrdata)
                                #print(encodedOutput.returncode)
                                #print("encodedOutput")

                                #play_sound.playAudioFile(serverPath + '/output/current_pic.wav')                        
                    '''
                    if False:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        if frameDiffCount == 0:  
                            frame2 = Image.open(io.BytesIO(frame))
                            frame2 = frame2.convert('L')
                            frame2Array = numpy.array(frame2)
                            frame2Matrix = numpy.matrix(frame2Array.reshape(width,height))
                            x_mean = frame2Matrix.mean(0).sum()/width
                            if x_max < x_mean :
                                x_max = x_mean

                            print(x_mean/x_max)
                            
                            
                            #frame1xList = get_avg_x(frame2Array, 200)
                            frame2.save(serverPath + '/output/current_pic.jpg')
                            frameDiffCount = 1
                        elif frameDiffCount >= 1:
                            frame3 = (Image.open(io.BytesIO(frame))).convert('L')
                            frame3.save(serverPath + '/output/current_pic2.jpg')
                            frameDiffCount = 0
                            frame = ImageChops.difference(frame2, frame3)
                            #frame = frame3
                            #width, height = absDiff.size
                            #frame = frame.convert('RGB')
                            imgBytes = io.BytesIO()
                            frame.save(imgBytes, 'BMP')
                            frame = imgBytes.getvalue()
                            frameDiffCount = 0
                            #s = 0
                            #for x in range(width):
                            #    for y in range(height):
                            #        r, g, b = rgb_im.getpixel((x, y))
                            #        s = r + g + b + s


                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                        
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')


                    '''
                    plain video out 
                    '''
                    if False:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        if frameDiffCount == 0:  
                            frame2 = Image.open(io.BytesIO(frame))
                            #frame2 = frame2.convert('RGB')
                            imgBytes = io.BytesIO()
                            frame2.save(imgBytes, 'BMP')
                            frame = imgBytes.getvalue()
                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                        
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')
                    if True:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        if frameDiffCount == 0:  
                            frame2 = Image.open(io.BytesIO(frame))
                            frame = frame2.convert('RGB')
                            frame = numpy.array(frame)
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            gray = cv2.GaussianBlur(gray, (21, 21), 0)
                     
                            # if the first frame is None, initialize it
                            if firstFrame is None:
                                firstFrame = gray
                                continue
                            # compute the absolute difference between the current frame and
                            # first frame
                            frameDelta = cv2.absdiff(firstFrame, gray)
                            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                     
                            # dilate the thresholded image to fill in holes, then find contours
                            # on thresholded image
                            thresh = cv2.dilate(thresh, None, iterations=2)

                            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                            cnts = imutils.grab_contours(cnts)
                     
                            # loop over the contours

                            for c in cnts:
                                    # if the contour is too small, ignore it
                                    if cv2.contourArea(c) < 95:
                                            continue
                     
                                    # compute the bounding box for the contour, draw it on the frame,
                                    # and update the text
                                    (x, y, w, h) = cv2.boundingRect(c)
                                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    text = "Occupied"
                                    print(x+w/2   ,'    ' ,y+h/2)
                                                
                            frame = Image.fromarray(frame)
                            imgBytes = io.BytesIO()
                            frame.save(imgBytes, 'BMP')
                            frame = imgBytes.getvalue()
                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                        
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')

        elif ".css" in self.path or ".js"  in self.path or ".log"  in self.path or ".txt"  in self.path or ".json"  in self.path or ".csv" in self.path   :
            PAGE = open(serverPath +'/'+ self.path[1:],'r').read()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            #self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))


            self.end_headers()
            self.wfile.write(content)

        elif ".wav" in self.path:
            print('start file')
            self.send_response(200)
            self.end_headers()
            with open(serverPath +'/'+ self.path[1:],'rb').read() as f:
                for l in f: self.sendall(l)
            self.close()
            print('done file')
        elif ".png" in self.path or ".jpg" in self.path :
            PAGE = open(serverPath + '/' + self.path[1:],'rb').read()
            content = PAGE
            self.send_response(200)
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(200)
            self.end_headers()

        #logging.info("Camera Crop: " , camera.crop)

        #logging.info("threshold: " , threshold)
        #logging.info("threshold: "+ length)
        
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def startCamera():
    global camera, output 
    print("starting")
    resolutionString = str(width)+'x'+str(height)
    with picamera.PiCamera(resolution=resolutionString, framerate=24) as camera:
        output = StreamingOutput()
        camera.start_recording(output, format='mjpeg')
        #camera.start_recording(output2, format='mjpeg')
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
            return camera
        finally:
            camera.stop_recording()




def get_avg_x(numpy_array, threshold=200):
    x_list = []
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            x_list[i] = (x_list[i] + numpy_array[i][j]) / 2
            
            
            #if numpy_array[i][j] > threshold:
            #    numpy_array[i][j] = 255
            #else:
            #    numpy_array[i][j] = 0
    return x_list


startCamera()
