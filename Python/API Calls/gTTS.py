# THIS WILL ONLY WORK ON WINDOWS
# For my raspberry pi version refer to https://github.com/learnICT/RPi-club/blob/master/TalkingPi/gTTS_on_The_Pi.py
# and read the readme file for installation

# import Google Text to Speech Python Library https://gtts.readthedocs.io/en/latest/
from gtts import gTTS
# import OS functions
import os

#This line calls the TTS function with a string and chosen language
tts = gTTS(text='Bir şarkısın sen. Ömür buyu sürecek.', lang='tr')
# This line saves the created MP3 to a file on your computuer
tts.save("good.mp3")
# This line will open and play the file.
os.system("good.mp3")
