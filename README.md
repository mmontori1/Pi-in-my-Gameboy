# Pi in my Gameboy
Raspberry Pi Gameboy Raspbian and RetroPie GUI

*This is a WIP. More details (and photos) coming soon!

#Intro
This is Jason Wozniak and Mariano Montori's HackIllinois 2017 project; We're trying to make a Gameboy out of a Raspberry Pi. The problem that we ran into during the event is that since we have the Raspberry Pi with both Raspbian and RetroPie, we needed an easy interface to run RetroPie. This simple TkInter based Python GUI is made to set up and run RetroPie on top of Raspbian without having to run any scripts, and instead just click a simple button to start it.

#Requirements
###Python 2.7 Dependencies

-TkInter

Note: TkInter already comes installed with Mac or Windows.

-PIL (Python Imaging Library)

To download using Mac, you can either download through brew or run these commands:
```
curl -O -L http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
tar -xzf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
python setup.py build
sudo python setup.py install
```
For more details, check out this link:

http://stackoverflow.com/questions/9070074/how-can-i-install-pil-on-mac-os-x-10-7-2-lion
