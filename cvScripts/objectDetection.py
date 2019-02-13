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
global encodeImage
encodeImage = False
area = (0,0,width,height)
triggerPixelBox = [0,0,5,5]
diffThresh = 40000
diffRate = 80
ampThresh = 200

s = -1
frame1xList = []
frame1yList = []
frame2xList = []
frame2yList = []
x_buffered = []
y_buffered = []
numReadings = 9 
x_total = -1
y_total = -1
readIndex = -1
for i in range(0,numReadings):
    x_buffered.insert(i, 0)

for i in range(0,numReadings):
    y_buffered.insert(i,0)

firstFrame = None
def getObjectFromFrame2(frame):
    frame3 = (Image.open(io.BytesIO(frame))).convert('L')
    frame3.save(serverPath + '/output/current_pic2.jpg')
    frameDiffCount = 0
    frame = ImageChops.difference(frame2, frame3)
    imgBytes = io.BytesIO()
    frame.save(imgBytes, 'BMP')
    frame = imgBytes.getvalue()

def encodeImage(frame):
    with output.condition:
        output.condition.wait()
        frame = output.frame
    self.wfile.write(b'--FRAME\r\n')
    self.send_header('Content-Type', 'image/jpeg')
    self.send_header('Content-Length', len(frame))
    self.end_headers()
    self.wfile.write(frame)
    self.wfile.write(b'\r\n')
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
        frame2 = Image.open(io.BytesIO(frame))
        frame2.save(serverPath + '/output/current_pic.jpg')
        
        image_encoder.encodeObject(serverPath + '/output/current_pic.jpg', './output/current_pic.wav','.75' )
        #stdoutdata, stderrdata = encodedOutput.communicate()

        #play_sound.playAudioFile(serverPath + '/output/current_pic.wav')                        
        
def getCenterOfObject(frame):
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
            frame2.save(serverPath + '/output/current_pic.jpg')
            frameDiffCount = 1
        elif frameDiffCount >= 1:
            frame3 = (Image.open(io.BytesIO(frame))).convert('L')
            frame3.save(serverPath + '/output/current_pic2.jpg')
            frameDiffCount = 0
            frame = ImageChops.difference(frame2, frame3)
            imgBytes = io.BytesIO()
            frame.save(imgBytes, 'BMP')
            frame = imgBytes.getvalue()
            frameDiffCount = 0
            #s = 0
            #for x in range(width):
            #    for y in range(height):
            #        r, g, b = rgb_im.getpixel((x, y))
            #        s = r + g + b + s

            self.wfile.write(frame)

    '''
    plain video out 
    '''
def getFrame(frame):
    with output.condition:
        output.condition.wait()
    frame = output.frame
    frame2 = Image.open(io.BytesIO(frame))
    imgBytes = io.BytesIO()
    frame2.save(imgBytes, 'BMP')
    frame = imgBytes.getvalue()
    return frame
def getxywh(frame):
    with output.condition:
        output.condition.wait()
    frame = output.frame
    frame2 = Image.open(io.BytesIO(frame))
    frame = frame2.convert('RGB')
    frame = numpy.array(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray
        continue
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts[1:]:
            if cv2.contourArea(c) < 10:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    frame = Image.fromarray(frame)
    imgBytes = io.BytesIO()
    frame.save(imgBytes, 'BMP')
    frame = imgBytes.getvalue()
    
 def getupdownleftright(frame):
    with output.condition:
        output.condition.wait()
    frame = output.frame
    frame2 = Image.open(io.BytesIO(frame))
    frame = frame2.convert('RGB')
    frame = numpy.array(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray
        continue
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts[1:]:
            if cv2.contourArea(c) < 10:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
    frame = Image.fromarray(frame)
    imgBytes = io.BytesIO()
    frame.save(imgBytes, 'BMP')
    frame = imgBytes.getvalue()
    return frame

def getavg(frame):
    with output.condition:
        output.condition.wait()
        frame = output.frame
    frame2 = Image.open(io.BytesIO(frame))
    frame = frame2.convert('RGB')
    frame = numpy.array(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray
        continue
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts[1:]:
            if cv2.contourArea(c) < 10:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)

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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
    frame = Image.fromarray(frame)
    imgBytes = io.BytesIO()
    frame.save(imgBytes, 'BMP')
    frame = imgBytes.getvalue()
    return frame
