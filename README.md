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







