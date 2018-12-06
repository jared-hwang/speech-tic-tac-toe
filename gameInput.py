# Jared Hwang (jhwang11) Jacob Bennert (jbenne06)
# gameInput.py
#
# Contains the microphone and methods to accept user input via speech 

import speech_recognition as sr
import vlc
import time
import simpleaudio as sa

class gameInput(object):
    
    def __init__(self):
        self._r = sr.Recognizer()


    def acceptInput(self, canvas):

        # canvas.swapGoLight()
        # canvas.repaint()


        with sr.Microphone() as source:
            print("Say something!")
            audio = self._r.listen(source)

        print("Parsing...")

        # self._canvas.swapGoLight()
        # self._canvas.repaint()

        # recognize speech using Google Speech Recognition
        try:
            print("You said: " + self._r.recognize_google(audio))
            # return self._r.recognize_google(audio)
        except sr.UnknownValueError:
            print("We could not recognize the audio")
            return False
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return False


        if self.acceptableInput(self._r.recognize_google(audio).lower()):
            return self._r.recognize_google(audio).lower()
        else:
            print("That is not an acceptable input. Please say again")
            return False



    def promptUser(self):
        player2 = vlc.MediaPlayer("makeMove.mp3")
        player2.play()

    def acceptableInput(self, input):
        acceptable = ["red", "yellow", "blue",
                      "purple", "pink", "white",
                      "turquoise", "green", "orange"]

        if input in acceptable:
            return True
        else:
            return False
