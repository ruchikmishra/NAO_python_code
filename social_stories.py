import pygame
import sys
import sys
from naoqi import ALProxy
import time
import almath
import csv
import pandas as pd


tts = ALProxy("ALTextToSpeech","192.168.1.132", 9559)
tts.setParameter("speed",85)



while(1):
    user_input = input("Which story?: ")

    if user_input==0:
        with open('happy.txt', 'r') as file:
            content1 = file.read()
            tts.say(content1)
            time.sleep(0.4)
##            tts.say("Great Job!")
    elif user_input==1:
        with open('sad.txt', 'r') as file:
            content2 = file.read()
            tts.say(content2)
            time.sleep(0.4)
##            tts.say("Great Job!")
    elif user_input==2:
        with open('scared.txt', 'r') as file:
            content3 = file.read()
            tts.say(content3)
            time.sleep(0.4)
##            tts.say("Great Job!")

