# spiPi -- An internet of things, object detection, artisticly interactive python websock camera for the raspberry pi and the picamera.

The purpose of the spiPi is to be a Webcontrolled Video camera that produces data from the images that are processed.
The picamera library has a variety of default filters and image enhacements, many of these are opimized to work directly with the hardware so it runs very fast.

https://picamera.readthedocs.io/en/release-1.13/

# the spiPi has two features, right now
By doing object detection with opencv, the camera sends the coordinates of these objects to a MQTT broker. Now that the feature data is out of the pi, there are a variety of functions and interesting interactions that we can do with it.
( Please see the Digital Culture Server, here https://github.com/sylatupa/Digital_Culture_Server ; and also look here for more examples of this data being consumed: Pure Data Synthesizer: https://github.com/sylatupa/Digital-Culture-Sound-Client & IOT Device https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32  

So, this camera allows for artistic sampling of video data, a transmission of that data using a contemporary protocol MQTT.

## Reasoning and Motivations
IOT and the arts:
There is so much support for raspberry pis and they are small enough to run off a battery (and they are inexpensive). This project tries to solve a few things:
* Turning video data into a readily available data source
* Be able to provide a direct solution to gathering video that is easy as buying something off the shelf, but provides many more benefits. For a variety of uses, such as:
-- Security of the home and business
-- Art and entertainment using video data that is collected live and in place (in situ)
-- Citizen science, for the collection of time lapse video.

Stand alone server benefits:
Stand alone wifi-router: This project uses an additional wifi-router that is plugged into my homes wifi router, so it is interntet connected. But, the benefit of having this additional router layer is that I can take it with me to bring the network into locations that wouldn't have accessible wifi. Getting a battery operated wifi could make this potentially able to be run anywhere.



## Getting Started


### Prerequisites

Networking:

Running headless:

### Installing

(spiPi_requirements.txt) https://gist.github.com/sylatupa/e74248aba2906976b52d9d6011b660de


## Running the tests

## Deployment
```
with venv being the virtual environment folder, type:
source venv/bin/activate

which opens the virtual environment: 
(venv)pi@spipi:~/spiPi $

then type:
python specrideo.py

Now open a browser and go the the ip address for the raspberry pi, and go to port 8000.

``` 
## Built With

* Python 3.4m
* virtualenv 
* opencv --this was the most difficult to install. But, please see the pip installation requirements. And, the list of installation steps are available in this project.

## Contributing

#(comment) Please read [CONTRIBUTING.md](https://gist.github.com/sylatupa/4d0b51c97d2bd8cf210a60c0e7a7d175) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **S P Y-M** - *Wrote and collected supporting code.
* Contributors:

## License

## Acknowledgments

https://picamera.readthedocs.io/en/release-1.13/
