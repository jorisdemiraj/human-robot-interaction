#https://www.youtube.com/watch?v=bOqcK8qTXkA&index=3&list=PLtl9EQhH8dm3cef90H7p1DKWODnkg0Abx
from gtts import gTTS
#import pyglet
import os

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'temp.mp3'
    file.save(filename)
    
    os.system("temp.mp3")

#    os.remove(filename)