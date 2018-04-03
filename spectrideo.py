import io
import picamera
import logging
import socketserver
from threading import Condition
import http.server as server
import os
from PIL import Image
print(os.getcwd())
import imgencode

#import spectrogram 
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
#output = ''


# CAMERA RESOLUTION
width = 640
height = 480

area = (0,0,width,height)
class StreamingHandler(server.BaseHTTPRequestHandler):
    global camera, output,x,y,w,h,effect_no,frame,area
    def do_GET(self):
        global x,y,w,h,effect_no,frame,area
        print(self.path)
        if self.path == '/':
            #self.send_response(200)
            #self.send_header('Location', '/index.html')
            self.path = '/index.html'
            #self.end_headers()
        elif 'chngCoor' in self.path:
            self.send_response(200)
            self.send_header('Location', '/index.html')
            self.end_headers()
            newCrd = list(map(float,self.path.split('?')[1].split(',')))
            crop = (newCrd[0]/width, newCrd[1]/height, newCrd[2]/width, newCrd[3]/height)
            camera.crop = crop
        elif 'rotate' in self.path:
            if self.path.split('?')[1] == 'right':
                camera.rotation = camera.rotation + 90
                #camera.resolution = str(height)+'x'+str(width)
            else:
                camera.rotation = camera.rotation - 90
                #camera.resolution = str(width)+'x'+ str(height)

        elif 'up' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'down' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'left' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'right' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'zoom_in' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'zoom_out' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])

        elif 'sharpness' in self.path:
            camera.sharpness =  int(self.path.split('?')[1])
        elif 'contrast' in self.path:
            camera.contrast =  int(self.path.split('?')[1])
        elif 'brightness' in self.path:            
            camera.brightness = int(self.path.split('?')[1])
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
        elif 'hflip' in self.path:
            camera.hflip = False
        elif 'vflip' in self.path:            
            camera.vflip = False



        if self.path == '/index.html':
            PAGE = open('bideo.html','r').read()
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
            tempo = 60
            tempoCount = 0
            count = 0
            if True:
            #try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
                    
                    if tempoCount == 600  :
                        print("making Sound Now nowwwww")
                        frame2 = Image.open(io.BytesIO(frame))
                        #foo = frame2.resize((60,40),Image.ANTIALIAS)
                        foo = frame2.resize((30,20),Image.ANTIALIAS)
                        foo.save('./output/current_pic.jpg')
                        frame2.save('./output/current_pic_quality.jpg')
                        
                        imgencode.start('./output/current_pic.jpg', './output/current_pic.wav',1 )
                        #spectrogram.start(foo, './80_150_'+str(count)+'_5.wav',1 )
                        tempoCount = 0
                        count = count + 1
                    tempoCount = tempoCount + 1

                """
            except Exception as e:
                logging.warning(
                        'Removed streaming client %s: %s',
                        self.client_address, str(e))
"""                
        elif ".css" in self.path or ".js" in self.path or "png" in self.path or "jpg" in self.path :
            PAGE = open(self.path[1:],'r').read()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            #self.send_header('Content-Type', 'text/html')
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


