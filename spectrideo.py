'''
sudo apt-get install libasound2-dev libasound2 libasound2-plugins
sudo apt-get install python-dev
sudo pipenv install pyaudio
sudo apt-get install libportaudio-dev
sudo apt-get install portaudio19-dev
sudo apt-get install pyaudio
sudo apt-get install numpy
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
import numpy
from PIL import Image
from PIL import ImageChops
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
#width = int(1366/8)
#height = int(768/8)
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
            if True: #True: #checking for frame difference is turned on
                #try:
                while True:
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


                    if True:
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
