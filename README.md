# Sweary Pi
Build a WiFi enabled, super annoying, super sweary swear machine using a Raspberry Pi!
## What Is It
Sweary Pi is a tool to play audio files remotely on a Raspberry Pi or similar. Install the server on the Pi and supply some audio, connect to it with the client then trigger the audio on the Pi remotely through the client. Websockets are used behind the scenes for super-responsive swearing!

The provided swears were obtained from [Buffy's Swearing Keyboard](https://www2.b3ta.com/buffyswear). There's no reason why you couldn't replace them with less sweary audio if you wanted though.

Please note that Sweary Pi is not production quality software. Care should therefore be taken if you wish to deploy it on a network where malicious actors may be present.
## Setting It Up
There are a few steps required to get everything up and running but you should only have to do most of them once.
### The Server
You should carry these steps out on the Pi or the computer that you want to hear the audio from. If it's not a Pi running Raspbian (which is what the instructions are written for) make sure `aplay` is on the path. Steps 4 and 5 can be skipped if you wish to use the supplied swears:
1. Install Python3 and Pip if they're not already installed by running the below commands in a terminal:
```
sudo apt-get update
sudo apt-get install python3 python3-pip
```
2. Clone the repo and navigate to the `server` folder once it's done:
```
git clone https://github.com/bmustill-rose/Sweary-Pi
cd Sweary-Pi/server
```
3. Install the required software: `pip3 install -r requirements.txt`.
4. If you don't want to use the supplied swears at this point you should source some audio and put the files into the server directory. For your first go I'd suggest sticking to wav files (files that have the .wav extension).
5. Sweary-Pi maps audio files to keyboard keys - "a" could be mapped to "a.wav" for example although you can name your audio files whatever you like. You now need to configure these mappings for the Sweary-Pi server. Open the `audioLookup.py` file in an editor of your choice. You should see something like the below:
```python
audioLookup = {
 "a": "a.wav",
 "b": "b.wav",
 "c": "c.wav",
 "d": "d.wav",
 "e": "e.wav",
 "f": "f.wav",
 "F": "F.wav"
}
```
There are a few things to note here:
- Each entry contains 2 things: the one on the right is the name of an audio file and the one on the left is the name of the key you want associated with it.
- Note that upper and lower cases of the same letter can trigger different audio files, as is the case with f.
- All of the values are wrapped in quotes and all but the last one finishes with a "," - It's important you follow the same conventions when you're making your own entries.
- You'll notice that the `audioLookup.py` file you downloaded has many more entries than the one above but not one for every character on your keyboard. This isn't an issue however as Sweary-Pi is smart enough to ignore keypresses on the client that it doesn't have audio files for.
Modify the `audioLookup.py` file based on your setup and save your changes.
6. Congratulations! It's now time to test the server. Run `python3 server.py` and look at the output. It should look something like this:
```
 * Serving Flask app 'server' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.0.78:5000/ (Press CTRL+C to quit)
```
If it does, make a note of the address that it's running on (192.168.0.75 in this case) and move on to the client section below. If it doesn't double check you've followed all the above steps correctly. If you have and it's still not working, consider filing an issue.
### The Client
The client runs on the computer you want to control the server from and is much easier to configure than the server. It should work on more or less any operating system that supports Python 3.
1. Check that Python3 and Pip are installed - steps to do this will vary from platform to platform. If it's not installed download it from the [Python downloads page](https://python.org/downloads).
2. Clone the repo and navigate to the client folder once it's done. If you don't have Git installed choose the download zip option on the Github website instead:
```
git clone https://github.com/bmustill-rose/Sweary-Pi
cd Sweary-Pi/client
```
3. Install the required software: `pip3 install -r requirements.txt`.
4. Run `python3 client.py address` where address is the number you noted above. If you're sure you've installed Python 3 but python3 isn't been found run `python` instead. If everything's worked correctly you should see something like:
```
Listening. Type a character or more and press enter or press control + c to quit
>
```
Press a key that you've mapped to a sound file then press enter. With any luck you should hear it from the device you configured the server on. If you don't double check that you've done everything correctly and if you feel you have, please file an issue.
### Run The Server on Boot
At the moment you'll have to manually start the server every time you reboot the Pi which isn't ideal for those situations where you just need a swear there and then. This section walks you through the steps required to make the server run every time the Pi reboots. Make sure you've successfully triggered audio through the client before you carry out this section:
1. Open a terminal and run `sudo nano /etc/rc.local`.
2. This file contains commands that will be run whenever the Pi is powered on / reboots. Scroll to the bottom where you should see a line like:
```bash
exit 0
```
3. Enter the below command above the exit 0 line, replacing values as described below:
```bash
su pi -c "cd /path/to/sweary-pi/server/folder && python3 server.py" &
```
- Replace "pi" with the user you set the server up under. If you're not sure stick with pi.
- Replace "/path/to/sweary-pi/server/folder" with the location of the server folder you cloned in the first section.
4. Reboot the Pi.
5. Once booted try to connect once again using the client. If everything's working properly it should function just as it did previously.
Congratulations! You've just built your very own Sweary Pi! Do feel free to continue customizing the audio but bear in mind that you'll need to restart the server and client every time you make a change.