import io
import picamera
import logging
import socketserver
from threading import Condition
import http.server as server

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
output = ''
class StreamingHandler(server.BaseHTTPRequestHandler):
    global camera, output,x,y,w,h,effect_no
    def do_GET(self):
        global x,y,w,h,effect_no
        if self.path == '/':
            self.send_response(200)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif 'chngCoor' in self.path:
            print('in')
            self.send_response(200)
            self.send_header('Location', '/index.html')
            self.end_headers()
            #camera.stop_recording()
            camera.crop = tuple(map(float,self.path.split('?')[1].split(',')))
        elif 'rotate' in self.path:
            
            camera.rotation =  int(self.path.split('?')[1])
            print(camera.rotation)
        elif 'sharpness' in self.path:
            if camera.sharpness >= 249:
                camera.sharpness = 0
            else:
                camera.sharpness =  camera.sharpness + 20
        elif 'contrast' in self.path:
            print(camera.contrast)
            if camera.contrast >= 100:
                camera.contrast = 0
            else:
                camera.contrast =  camera.contrast + 5            
        elif 'brightness' in self.path:            
            print(camera.brightness)
            if camera.brightness >= 100:
                camera.brightness = 0
            else:
                camera.brightness =  camera.brightness + 5            

        elif 'saturation' in self.path:            
            print(camera.saturation)
            if camera.saturation >= 100:
                camera.saturation = 0
            else:
                camera.saturation =  camera.saturation + 5 
        elif 'ISO' in self.path:            
            camera.ISO = 1 
        elif 'video_stabilization' in self.path:
            camera.video_stabilization = False

            #camera.exposure_compensation = 0
            #camera.exposure_mode = 'auto'
            #camera.meter_mode = 'average'
            #camera.awb_mode = 'auto'
        elif 'image_effect' in self.path:
            keys = list(camera.IMAGE_EFFECTS.keys())
            if len(keys) >= effect_no:
                print(keys)
                camera.image_effect = keys[effect_no]
                effect_no = effect_no + 1
            else:
                effect_no = 0
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
        
            try:
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
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_response(200)

            #self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def startCamera(crop):
    global camera, output
    with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
        output = StreamingOutput()
        #Uncomment the next line to change your Pi's Camera rotation (in degrees)

        #camera.rotation = 90
        print('here')

        #camera.crop = (.4,.4,.3,.3)
        camera.start_recording(output, format='mjpeg')
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
            return camera
        finally:
            camera.stop_recording()

startCamera((0,0,1,1))
    



