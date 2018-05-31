#!/usr/bin/python
from PIL import Image
import math, wave, array, sys, getopt
import logging
logging.basicConfig(filename='loggingEncoder.log',level=logging.DEBUG)
logging.debug('Debug Image Encoding Script ')
#logging.info('')
def start(inputfile, outputfile, duration):
    try:
        logging.debug('Starting the make of sound; in pic to out wav')
        im = Image.open(inputfile)
        width, height = im.size
        rgb_im = im.convert('RGB')
        durationSeconds = float(duration) 
        tmpData = []
        maxFreq = 0
        data = array.array('h')
        channels = 1
        sampleRate = 44100 #max freq = 20kHz
        sampleRate = 22050 #max freq = 10kHz
        sampleRate = 11025 #max freq = 5kHz
        sampleRate = 8000 #max freq = 3.6kHz
        #https://wiki.audacityteam.org/wiki/Sample_Rates
        dataSize = 2 
        numSamples = int(sampleRate * durationSeconds)
        samplesPerPixel = math.floor(numSamples / width)
        C = 20000 / height #rate 44100
        C = 10000/ height #rate 22050
        C = 5000/ height #rate 11025
        C = 3600 / height #rate 8000
        C = 3850 / height #(bumped it up abit from 3.6                 
        logging.debug('starting encoding loops')
        for x in range(numSamples):
            rez = 0
            
            pixel_x = int(x / samplesPerPixel)
            if pixel_x >= width:
                pixel_x = width -1
                
            for y in range(height):
                r, g, b = rgb_im.getpixel((pixel_x, y))
                s = r + g + b
                if s < 500:
                    s = 0

                volume = s * 100 / 2000#765
                
                if volume == 0:
                    continue
                
                freq = int(C * (height - y + 1))
                
                rez += getData(volume, freq, sampleRate, x)

            tmpData.append(rez)
            if abs(rez) > maxFreq:
                maxFreq = abs(rez)
        
        for i in range(len(tmpData)):
            data.append(int(32767 * (tmpData[i] / maxFreq)))
        logging.debug('saving encoding')
        f = wave.open(outputfile, 'w')
        f.setparams((channels, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
        f.writeframes(data.tostring())
        f.close()
    except Exception as e:
        logging.debug("error: " + e)
    except:
        logging.debug("error exceptions")
#THIS IS THE COOL PART---MATH.PI IS THIS A GAUSIAN DISTRIBUTION OF THE FREQ?
def getData(volume, freq, sampleRate, index):
    return int(volume * math.sin(freq * math.pi * 2 * index /sampleRate))

if __name__ == '__main__':
    logging.debug('start imgencode script: ' + str(sys.argv))
    try:
        start(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as e:
        logging.debug('errors: ' + str(e))
    except:
        logging.debug('more errors')
    logging.debug('END IMG ENCODE')

    """
    inputfile = ''
    outputfile = ''
    duration = ''
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:t:")
    except getopt.GetoptError:
        print('imgencode.py -i <input_picture> -o <output.wav> -t <duration_seconds>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('imgencode.py -i <input_picture> -o <output.wav> -t <duration_seconds>')
            sys.exit()
        elif opt == "-i":
            inputfile = arg
        elif opt == "-o":
            outputfile = arg
        elif opt == "-t":
            duration = arg
imgs = ('./image1',
        './image2',
        './image4',
        './image6',
        './image10'
        )
import os
print(os.getcwd())
for ele in imgs:
    print(ele)
    start(ele+'.jpg', ele+'_w_color_jpg.wav', 2)
    """
