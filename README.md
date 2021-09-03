# SoundBox to play random THE OFFICE quotes
A guide to create a Sound Box on button press with a Raspberry Pi. I used Pi 4 B 4GB model but the setup is generic.

Final outcome: https://www.youtube.com/watch?v=zevo9r89HpU
<p align="center">
  <img alt="soundbox" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/final_inside_case.jpg" width="25%">
</p>


## Goal
I wanted to create a portable box like thing. Person connects power and presses a button to hear a quote from [The Office](https://www.imdb.com/title/tt0386676/)

### Things to Buy beforehand
- A working Raspberry Pi
    - i used a Pi 4 B but the code should run on all
- A sound output (speaker, earphone)
    - Any speaker with a 3.5mm Jack or a headphone is portable i guess
- A button
    - i bought a pre soldered button for  ease of use, but choice is free
- wires and breadboard for testing
    - ducant wires for easy contact with boards
- electric tape, solder setup or any other way you have to connect the wire to the GPIO box

<p align="center">
  <img alt="speaker" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/mini_speaker_example.jpg" width="15%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Button" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/pre-soldered_button_example.jpg" width="25%">
</p>

You will also need a monitor, mouse and keyboard to do the initial setup

## MAIN FLOW
1) Acquire sound samples
2) Write code (Python)
3) Initial Setup of Pi and Test with breadboard
4) Test directly removing breadboard
5) Prepare as a service to run without a monitor

### Acquire sounds

First get your mp3 sounds into a folder. 
Then convert all to wav using inbuilt library. Mp3 is not always recognized by the library.
```
$ ls
1.mp3
2.mp3
3.mp3

# convert 
$ for f in *.mp3; do ffmpeg -i "$f" "$f%%.*}.wav"; done
$ rm *.mp3

$ ls
1.wav
2.wav
3.wav

```
At this point you should ensure the sound clips are ok. Use the following
```
# trim
# eg trip from 1 to 7.5 secs
$ ffmpeg -i sound.wav -ss 1 -to 7.5 -c copy test.wav 

# change volume. NOT RECOMMENDED . Voices become weird
$ ffmpeg -i input.wav -filter:a "volume=10dB" output.wav
```

### Prepare Code

The code is at [the_office_soundbox.py](https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/the_office_soundbox.py).
Main part is done using [pygame mixer](https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_volume) and [gpiozero](https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box)

Points of note:
- we write the files in a dictionary and add a  default sound.
- We use `mixer.music.load` as it stops the current playing sound. This prevents sound overlap.
- We use time.sleep(0.5) at the end to ensure no rapid button presses trouble the not so robust system here

! The only vital thing to set in the code is the GPIO pin which is the pin where you connected the red wire of your button. This is important as it will be the sole input.
```
button = Button(16)
# I am using pin 16 on the board
```

Please refer to your manual for pin and corresponding GPIO pin number

### Setup the circuit

First you should follow the box setup to run your Pi initially. connect the heat sinks, case and run on PC.

Now we add a breadboard and button with wires. Main thing to remember is red to GPIO, black to GND. My setup has GPIO in pin 16.

Left image stolen from here
https://projects.raspberrypi.org/en/projects/button-switch-scratch-pi/1

<p align="center">
  <img alt="diag" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/button_basic.png" width="35%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="real_breadboard" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/initial_setup.jpg" width="35%">
</p>

Now turn on the device and to test if it works.

1) Run your code
```
$ python3 the_office_soundboard.py
...
```
2) press the button you attached

## Test directly removing breadboard
Next test it runs without the breadboard. Basically remove the breadboard and connect the wires directly. I have used a hack but you should use electrical tape or soldering.

<p align="center">
  <img alt="without_breadboard" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/after_removing_breadboard.jpg" width="35%">
</p>

## Run without Monitor
You need to deploy the code as a service to have it booted automatically everytime you start the Pi.
Please refer here:
https://www.raspberrypi.org/documentation/computers/using_linux.html#the-systemd-daemon
My sample file is here:
https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/office_soundboard.service

Start the service or restart your Pi .
on restart you should not have to run the code using python3 anymore. Pressing the button should work.

Now try after removing monitor, mouse keyboard

#### Pi4 gotchas
Pi 4 does not boot properly if there is no monitor attached.
You need to boot in CLI mode and/or set a default Resolution.

https://www.digikey.com/en/maker/blogs/2018/how-to-boot-to-command-line-and-ssh-on-raspberry-pi
```
$ sudo raspi-config
# menu may change

# 1 set boot CLi
System > Boot > CLi with login

# Set resolution
Display > REsolution > choose any

Now choose Finish
``

Remember to rever both these when you want to tinker around in GUI again.
