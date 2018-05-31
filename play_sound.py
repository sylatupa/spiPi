#nice.
import logging
import pyaudio  
import wave  

#import imutils
import numpy
import subprocess
#from multiprocessing import Pool
#import os
count = 1
#import itertools
import os


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='logging.log',level=logging.DEBUG)
def pyAudioOut(filename):
    f = wave.open(r"./output/current_pic.wav","rb")  
    p = pyaudio.PyAudio()
    logging.debug('{} {}'.format( p.get_format_from_width(f.getsampwidth()), f.getframerate() ))
    #print('format_width: ' , p.get_format_from_width(f.getsampwidth()))
    #print('channels: ',f.getnchannels())
    print('framerate', f.getframerate()  )
    chunk = int(f.getframerate()/2)

    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            channels = f.getnchannels(),  
            rate = f.getframerate(),  
            output = True)  
    data = f.readframes(chunk)  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
    stream.stop_stream()  
    stream.close()  
    p.terminate()


class play_sound(object):
    def __init__(self):
        self.p = ''
        self.pid = ''
        pass


    def playAudioFile(self, AudioFile):
        featureSetProcess =  ['play','-n','-G',AudioFile, 'gain','-5']
        featureSetProcess =  ['play',AudioFile, 'gain','+7']

        #effects = ['fade','h' , '0', '1','.1']
        #delay = ['delay', '1.3', '1' , '.76', '.54', '.27']
        #repeat = ['repeat', '10']
        playThis = featureSetProcess #+ effects + delay + repeat
                #process =  ['play','-n','synth','.6', 'sine', '333','sine',str(note), 'pl', str(note)]
                #process = ['play','-n','synth','333','sine',str(note), 'sine', str(note), 'fade', '0', '1']
        #p = subprocess.Popen(playThis, stdout=subprocess.PIPE, shell=True)
        #subprocess.Popen(['ps', '-ef', '|' ,'grep','sox'])
        #ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
        #output = subprocess.check_output(('grep', 'python'), stdin=ps.stdout)
        #print ps
        #print output
        #ps.wait()
        #
        if self.pid == '' or os.path.lexists('/proc/%s' % self.pid) == False or True:
            FNULL = open(os.devnull, 'w')
            self.p = subprocess.Popen(playThis, stdout=FNULL, stderr=FNULL, close_fds=True)
            self.pid = self.p.pid
            return self.p
        else:
            pass
        #self.p.kill()
            #FNULL = open(os.devnull, 'w')
            #self.p = subprocess.Popen(playThis, stdout=FNULL, close_fds=True)            
        """
        try:
            subprocess.check_output(playThis)
        except: 
            print "*********SUB PROCESS FAIL*****************"
        """
#        play -n synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1
          #subprocess.check_output(['play','-n','synth','2','pluck',str(note)])
    """def hello_world():
    URL = 'https://traffic.libsyn.com/democracynow/dn%d-%02d%02d-1.mp3'%(x.year,x.month,x.day)
    sonifyData.playPODCast(URL)
    t = Timer(secs, hello_world)
    t.start()
#https://gist.github.com/alexbw/1187132
#https://stackoverflow.com/questions/24072765/timer-cannot-restart-after-it-is-being-stopped-in-python
    """


    def playPODCast(self, URL):
        featureSetProcess =  ['play','-t','mp3',URL]
        playThis = featureSetProcess #+ effects + delay + repeat
        process_string =''
        for ele in playThis:
            process_string = process_string + ' ' + ele
        print('subprocess string: ', process_string)
        try:
            subprocess.check_output(playThis)
        except: 
            print( "*********SUB PROCESS FAIL*****************")

