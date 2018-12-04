import speech_recognition as sr
import vlc
import time

class gameInput(object):
    
    def __init__(self):
        self._r = sr.Recognizer()


    def acceptInput(self):
        time.sleep(1.5)
        with sr.Microphone() as source:
            print("Say something!")
            audio = self._r.listen(source)

        print("Parsing...")

        # recognize speech using Google Speech Recognition
        try:
            print("You said: " + self._r.recognize_google(audio))
            return self._r.recognize_google(audio)
        except sr.UnknownValueError:
            print("We could not recognize the audio")
            return False
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def promptUser(self):
        player2 = vlc.MediaPlayer("makeMove.mp3")
        player2.play()