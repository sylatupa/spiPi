# spectridio can be found here:
# https://github.com/sylatupa/spiPi

import io
try:
    import picamera
except ImportError:
    is_picamera = True
import mqtt_client.mqtt_client as mqtt_client


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
import statistics

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
width = 240 
height = 200
#width = int(1366/4)
#height = int(768/4)
frameDiffCount = 0
play_sound = ps.play_sound()
image_encoder = imgencode_proc.encoder()
image_processor = imgprocessing_proc.processor()
global encodeImage, frameDeltaMin, smallestContour, showDelta
encodeImage = False
area = (0,0,width,height)
triggerPixelBox = [0,0,5,5]
diffThresh = 40000
diffRate = 80
frameDeltaMin = 30
smallestContour = 120
showDelta = False
ampThresh = 200
class StreamingHandler(server.BaseHTTPRequestHandler):
    global camera, output,x,y,width,height,effect_no,frame,area, encodeImage, frameDiffCount, diffThresh, showDelta
    def do_GET(self):
        global x,y,width,height,effect_no,frame,area,frameDiffCount, frameDeltaMin, smallestContour, showDelta
        serverPath = os.path.dirname(os.path.realpath(__file__))
        if self.path == '/' or self.path == '/index.html':
            PAGE = open(serverPath + '/index.html','r').read()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
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

        elif 'showDelta' in self.path:
            self.send_response(200)
            self.end_headers()
            if showDelta==False:
                showDelta = True
            else:
                showDelta=False



        elif 'smallestContour' in self.path:
            smallestContour = int(self.path.split('?')[1])


        elif 'frameDeltaMin' in self.path:
            frameDeltaMin = int(self.path.split('?')[1])

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
            y_buffered = []
            numReadings = 20 
            x_total = 0
            y_total = 0
            readIndex = 0
            for i in range(0,numReadings):
                x_buffered.insert(i, 0)

            for i in range(0,numReadings):
                y_buffered.insert(i,0)
            
            x_max = 0
            firstFrame = None
            if True: #True: #checking for frame difference is turned on
                #try:
                while True:
                    if True:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        if frameDiffCount == 0:  
                            frame2 = Image.open(io.BytesIO(frame))
                            frame = frame2.convert('RGB')
                            frame = numpy.array(frame)
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            #gray = cv2.GaussianBlur(gray, (21, 21), 0)
                     
                            # if the first frame is None, initialize it
                            if firstFrame is None:
                                firstFrame = gray
                                continue
                            # compute the absolute difference between the current frame and
                            # first frame
                            frameDelta = cv2.absdiff(firstFrame, gray)
                            thresh = cv2.threshold(frameDelta, frameDeltaMin, 255, cv2.THRESH_BINARY)[1]
                            # dilate the thresholded image to fill in holes, then find contours
                            # on thresholded image
                            thresh = cv2.dilate(thresh, None, iterations=2)
                            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                            cnts = imutils.grab_contours(cnts)
                            #frame = cv2.drawKeypoints(gray, blobs, numpy.array([]), (0,0,255))#, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                            # Show keypoints
                            if showDelta:
                                frame = thresh
                            for c in cnts[:1]:
                                    print(len(cnts), " " , len(cnts[:4]))
                                    # if the contour is too small, ignore it
                                    if cv2.contourArea(c) < smallestContour:
                                            continue
                                            break
 
                                    # compute the bounding box for the contour, draw it on the frame,
                                    # and update the text
                                    (x, y, w, h) = cv2.boundingRect(c)
                                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    #mqtt_client.publish_data2("spyPi/object/x",x)
                                    #mqtt_client.publish_data2("spyPi/object/y",y)
                                    #mqtt_client.publish_data2("spyPi/object/w",w)
                                    #mqtt_client.publish_data2("spyPi/object/h",h)

                                    x_total = x_total - x_buffered[readIndex]
                                    x_buffered[readIndex] = x+w/2
                                    x_total = x_total + x_buffered[readIndex]
                                    readIndex = readIndex + 1

                                    y_total = y_total - y_buffered[readIndex]
                                    y_buffered[readIndex] = y+h/2
                                    y_total = y_total + y_buffered[readIndex]
                                    readIndex = readIndex + 1
                                    if readIndex >= numReadings:
                                        readIndex = 0
                                        #send now
                                        mqtt_client.publish_data2("spyPi/object/x_avg", statistics.median(x_buffered))
                                        mqtt_client.publish_data2("spyPi/object/y_avg", statistics.median(y_buffered) )
                                        #mqtt_client.publish_data2("spyPi/object/y_avg", y_total/numReadings)

                                                
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

startCamera()
