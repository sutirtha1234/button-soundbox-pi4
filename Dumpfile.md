# This is to dump code in before i clean it up

### Audio

```
# convert 
$ for f in *.mp3; do ffmpeg -i "$f" "$f%%.*}.mp3"; done

# trim
# eg trip from 1 to 7.5 secs
$ ffmpeg -i sound.wav -ss 1 -to 7.5 -c copy test.wav 

change volume
$ ffmpeg -i input.wav -filter:a "volume=10dB" output.wav

```
# Prep
```
$ i=1
$ for file in *.wav; do echo "$i: '$file',"; ((i++)); done;
1: '1.wav',
2: '2.wav',
3: '3.wav',
4: 'x.wav',

--> 
SOUND_DICT = {
    'default': '1.wav',
    1: '1.wav',
    2: '2.wav',
    3: '3.wav',
    4: 'x.wav'
}
```
Main Code
```
from gpiozero import Button
from datetime import datetime
import sys
import time
import random
from pygame import mixer

# The GPIO pin number where Red wire of Button is connected
button = Button(16)
mixer.init()
mixer.music.set_volume(0.9)
TOP_DIRECTORY = "/home/pi/Music/office_quotes/"

SOUND_DICT = {
    'default': '1.wav',
    1: '1.wav',
    2: '2.wav',
    3: '3.wav',
}
# No of songs = No of dict entries - One default entry
SONG_COUNT = len(SOUND_DICT) - 1
DEFAULT_SOUND = TOP_DIRECTORY + SOUND_DICT['default']

def pressed_action():
    choice = random.randint(1,SONG_COUNT)
    sound_file = TOP_DIRECTORY + SOUND_DICT[choice]
    print('Playing sound clip:', sound_file)
    
    try:
        # Preps file to play. Stops stream already playing
        mixer.music.load(sound_file)
        mixer.music.play()
    except Exception:
        print('Exception occurred when playing: ', sound_file)
        print('Playing default sound clip:', DEFAULT_SOUND)
        mixer.music.load(DEFAULT_SOUND)
        mixer.music.play()
    
    # Skippable. Ensures printing to journalctl immediately for debugging
    # Is useful to check logs when running this program as a sevice
    sys.stdout.flush()
    # Prevents quick multi presses of button
    time.sleep(0.5)

while True:
    button.when_pressed = pressed_action


```


# Main steps
1) Buy a basic Raspberry Pi system
2) Buy necessary components:
    - output sound
    - button
    - wires
3) get some audio samples
4) 
