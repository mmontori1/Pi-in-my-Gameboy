# Pi in my Gameboy
A Raspberry Pi GUI to boot up RetroPie through Raspbian

# Intro

This is an extension to Jason Wozniak and Mariano Montori's HackIllinois 2017 Hardware project; We're trying to make a Gameboy using the Raspberry Pi 3, putting all the pieces together into one Gameboy Case. Our goal is to have not only the usual Gameboy buttons, but also 2 extra analog sticks and shoulder buttons to take advantage of the Raspberry Pi 3 in order to play N64 and PS1 games as well, all on the go!

# Project Description

The problem that we ran into during the event is that since we have the Raspberry Pi with both Raspbian and RetroPie, we needed an easy interface to run RetroPie without having to use a keyboard to run scripts to start the emulator. This simple TkInter based Python GUI is made to set up and run RetroPie on top of Raspbian without having to run any scripts, and instead just click a simple button to start it.

# Requirements

### Raspberry Pi Requirements

-[Raspbian](https://www.raspberrypi.org/downloads/raspbian/)

-[RetroPie](https://retropie.org.uk/download/)

To use this project, we recommend to download and write these two images to your Raspberry Pi's SD card (links above). We have Raspbian Jessie with Pixel and the RetroPie Raspberry Pi 3 images. Check out this setup guide to write to the SD card.

[RPi SD card setup guide](http://elinux.org/RPi_Easy_SD_Card_Setup#SD_card_setup)

### Python 2.7 Dependencies

#### On your Laptop

-os

-subprocess

-TkInter

Note: os and subprocess are standard python modules

Note: TkInter already comes installed on Mac and Windows.

-PIL (Python Imaging Library)

To download using Mac, you can either download through brew or run the commands below. For more details, check out this [stackoverflow link](http://stackoverflow.com/questions/9070074/how-can-i-install-pil-on-mac-os-x-10-7-2-lion).
```
curl -O -L http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
tar -xzf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
python setup.py build
sudo python setup.py install
```

#### On the Raspberry Pi

In order for all the dependencies to work on the Raspberry Pi, you must have TkInter and Pillow installed. To do this, we had to run these commands through LXTerminal.

```
sudo apt-get install python-dev
sudo apt-get install tk8.6-dev tcl8.6-dev
sudo apt-get install python-imaging-tk
sudo pip install Pillow --upgrade
```
