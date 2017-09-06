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

```
git clone https://github.com/jasperproject/jasper-client.git
```

```
sudo apt-get install python-pip python-dev
sudo pip install --upgrade setuptools
sudo pip install -r jasper-client/client/requirements.txt
```

Install Pocketsphinx:

```
sudo apt-get update
sudo apt-get install pocketsphinx python-pocketsphinx
```

Install CMUCLMTK:

```
sudo apt-get install subversion autoconf libtool automake gfortran g++ --yes
```

```
svn co https://svn.code.sf.net/p/cmusphinx/code/trunk/cmuclmtk/
cd cmuclmtk/
./autogen.sh && make && sudo make install
cd ..
```


Install Phonetisaurus, m2m-aligner and MITLM:

```
wget http://distfiles.macports.org/openfst/openfst-1.3.4.tar.gz
wget https://github.com/mitlm/mitlm/releases/download/v0.4.1/mitlm_0.4.1.tar.gz
wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/m2m-aligner/m2m-aligner-1.2.tar.gz
wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/phonetisaurus/is2013-conversion.tgz

tar -xvf m2m-aligner-1.2.tar.gz
tar -xvf openfst-1.3.4.tar.gz
tar -xvf is2013-conversion.tgz
tar -xvf mitlm_0.4.1.tar.gz
```

```
cd openfst-1.3.4/
sudo ./configure --enable-compact-fsts --enable-const-fsts --enable-far --enable-lookahead-fsts --enable-pdt
sudo make install
```

```
cd m2m-aligner-1.2/
sudo make
cd ..
```

```
cd mitlm-0.4.1/
sudo ./configure
sudo make install
cd ..
```

```
cd is2013-conversion/phonetisaurus/src
sudo make
cd
```

```
sudo cp ~/m2m-aligner-1.2/m2m-aligner /usr/local/bin/m2m-aligner
sudo cp ~/is2013-conversion/bin/phonetisaurus-g2p /usr/local/bin/phonetisaurus-g2p
```

Build the Phonetisaurus FST model:

```
wget https://www.dropbox.com/s/kfht75czdwucni1/g014b2b.tgz
tar -xvf g014b2b.tgz
```

```
cd g014b2b/
./compile-fst.sh
cd ..
```

```
mv ~/g014b2b ~/phonetisaurus
```


Install dependencies for Julius STT engine:
