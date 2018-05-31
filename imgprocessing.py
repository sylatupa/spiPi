#!/usr/bin/python
from PIL import ImageChops
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
        logging.debug('starting encoding loops')
        s = 0
        for x in range(width):
            #rez = 0
            #pixel_x = int(x / samplesPerPixel)
            if pixel_x >= width:
                pixel_x = width -1
                
            for y in range(height):
                r, g, b = rgb_im.getpixel((x, y))
                s = r + g + b + s
    except:
        pass
    return s

        """
    except Exception as e:
        logging.debug("error: " + e)
    except:
        logging.debug("error exceptions")
if __name__ == '__main__':
    logging.debug('start imgencode script: ' + str(sys.argv))
    try:
        logging.debug('in try')
        start(sys.argv[1],sys.argv[2])
        logging.debug('in try')        
    except Exception as e:
        logging.debug('exception')
        logging.debug('errors: ' + str(e))
    except:
        logging.debug('except')
        logging.debug('more errors')
    logging.debug('END IMG ENCODE')

