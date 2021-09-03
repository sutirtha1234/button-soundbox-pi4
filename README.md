# SoundBox to play random THE OFFICE quotes
A guide to create a Sound Box on button press with a Raspberry Pi. I used Pi 4 B 4GB model but the setup is generic.

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
- electric tape, solder setup or any other way you have to connect the wire to the GPIO box

<p align="center">
  <img alt="Light" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/mini_speaker_example.jpg" width="15%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark" src="https://github.com/sutirtha1234/button-soundbox-pi4/blob/main/assets/pre-soldered_button_example.jpg" width="25%">
</p>

You will also need a monitor, mouse and keyboard to do the initial setup

## MAIN FLOW
1) Acquire sound samples
2) Write code (Python)
3) Test with breadboard
4) Test directly
5) Prepare as a service to run without a monitor

#### Acquire sounds

First get your mp3 sounds into a folder. 
Then convert all to wav using inbuilt library. Mp3 is not always recognized by the library.
```
$ ls
1.mp3
2.mp3
3.mp3

# convert 
$ for f in *.mp3; do ffmpeg -i "$f" "$f%%.*}.wav"; done

$ ls
1.mp3
2.mp3
3.mp3
1.wav
2.wav
3.wav

# rm *.mp3
```
