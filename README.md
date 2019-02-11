#spiPi -- a python websock camera for the raspberry pi and the picamera.

The purpose of the spiPi is to be a Webcontrolled Video camera that produces data from the images that are processed.
The picamera library has a variety of default filters are image enhacements, many of these are opimized to work directly with the hardware
in the webinterface Video is processed by the picamera so

DC Server is to be an MQTT broker and IOT automation hub. 
The services that it will provide is being an MQTT client, and converting some of the MQTT topics into UDP messages.
The benefit of converting some messages to UDP is that they can more easily be consumed by Pure Data and Max MSP.
So, this server allows for artistic expression of IOT data and use of IOT devices.

Based off of Node Red because of its ease of use and support, as well as the web based graphic interface. 

To convert MQTT to UDP, there is a standalone python script that is a MQTT broker and converts to UDP, if Node Red installation is not necessary or desirable.
This implementation will be done on a Raspberry Pi.

## Reasoning and Motivations
IOT and the arts:
Stand alone server benefits:
Stand alone wifi-router: This project uses an additional wifi-router that is plugged into my homes wifi router, so it is interntet connected. But, the benefit of having this additional router layer is that I can take it with me to bring the network into locations that wouldn't have accessible wifi. Getting a battery operated wifi could make this potentially able to be run anywhere.



## Getting Started

On many Pi OS images there is Node-Red already installed. It can be started from the terminal by typing node-red. The server will start and tell you the ip address that its running on, like:  [info] Server now running at http://127.0.0.1:1880/. Because we gave the Pi a reserved ip on the wifi router, and my laptop is using the same network, I open the Node-Red web interface using the Pis ip, and the port 1880. 


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Networking:
1) Standalond wifi-router, with Pi plugged directly into the ethernet.
2) Adjust the DHCP Reservation of the router to give the Pi a static ip, a reserved ip address.

Running headless:

Running Mosquitto Broker automatically on boot


```
Give examples
```

### Installing

At the time of writing this, Node-Red on a Pi was at version 15.3. 
Node-Red is typically on a Raspberry Pi already. But, before you get started developing with it--upgrade it by running:

```
sudo apt-get install --only-upgrade nodered
```

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

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

# (comment) Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **S P Y-M** - *Wrote and collected supporting code.
* Contributors:

## License

## Acknowledgments

https://picamera.readthedocs.io/en/release-1.13/
