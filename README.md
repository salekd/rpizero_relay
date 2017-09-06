# rpizero_relay

Cayenne

Run the following commands in order to avoid the error described here http://community.mydevices.com/t/build-for-python-3-4-2-failed-n/1540

```
sudo apt-get update
sudo apt-get -f upgrade
```

Run the installation script.

```
wget https://cayenne.mydevices.com/dl/rpi_840ukp8a2s.sh
sudo bash rpi_840ukp8a2s.sh -v
```

WebIOPi is part of the installation, you should see the following lines:

```
WebIOPi successfully installed
* To start WebIOPi foreground    : sudo webiopi [-h] [-c config] [-l log] [-s script] [-d] [port]

* To start WebIOPi background    : sudo /etc/init.d/webiopi start
* To start WebIOPi at boot    : sudo update-rc.d webiopi defaults

* Look in /tmp/webiopi/examples for Python library usage examples
```


Audio

http://jasperproject.github.io/documentation/installation/

```
sudo apt-get install git-core python-dev bison libasound2-dev libportaudio-dev python-pyaudio
```


Create file /lib/modprobe.d/jasper.conf

```
# Load USB audio before the internal soundcard
options snd_usb_audio index=0
options snd_bcm2835 index=1

# Make sure the sound cards are ordered the correct way in ALSA
options snd slots=snd_usb_audio,snd_bcm2835
```


Jasper
