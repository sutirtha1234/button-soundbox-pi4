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
