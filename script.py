from flask import Flask, render_template, request
from playsound import playsound
from pynput.keyboard import Listener
import random 
import keyboard
import time as t

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route('/index')
def index():
        return render_template('home.html')

@app.route('/examination')
def examination():
        song_number = random.randint(1,4)
        playsound('audio_files/' + str(song_number) + '.mp3')
        #start_time = t.time()
        
        def key_press(key):
                print(key.name)
                keyboard.on_press(key_press)
        while True:
                t.sleep(1)
        return "examination screen"


@app.route('/results')
def results():
    return "results screen"

if __name__ == "__main__":
    app.run(debug=True)


