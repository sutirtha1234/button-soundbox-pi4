from gpiozero import Button
from datetime import datetime
import sys
import time
import random
from pygame import mixer

# initial sound settings
mixer.init()
mixer.music.set_volume(0.9)

# UPDATE: The GPIO pin number where Red wire of Button is connected
button = Button(16)
# UPDATE: Use directory of where your sounds are stored
TOP_DIRECTORY = "/home/pi/Music/soundbox_sounds/"

# generated with below command. Or hand write every sound file name.
# bash$ i = 1
# bash$ for file in *.wav; do echo "$i: '$file',"; ((i++)); done;
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
