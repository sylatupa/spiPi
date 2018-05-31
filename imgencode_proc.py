#nice.
import pyaudio  
import wave  
import logging
import numpy
import subprocess
import os
import sys
logger = logging.getLogger(__name__)
#logger.debug('outIMGdebug')
#logger.info('outIMGinfo')
#logger.warning('outIMGwarning')
count = 1
def pyAudioOut(filename):
    logger.debug('{} {}'.format( p.get_format_from_width(f.getsampwidth()), f.getframerate() ))
class encoder(object):
    def __init__(self):
        self.p = ''
        self.pid = ''
        pass


    def encodeObject(self, ImageFile, AudioFile, seconds):
        logger.debug('starting encoding subprocess')
        featureSetProcess =  ['python3', './imgencode.py',ImageFile, AudioFile, seconds]

        if self.pid == '' or os.path.lexists('/proc/%s' % self.pid) == False or True:
            logger.debug('running: ' + str(featureSetProcess))
            FNULL = open(os.devnull, 'w')
            self.p = subprocess.Popen(featureSetProcess, stdout=FNULL, stderr=FNULL, close_fds=True)
            self.pid = self.p.pid
            return self.p
        else:
            logger.debug('else statement')
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

