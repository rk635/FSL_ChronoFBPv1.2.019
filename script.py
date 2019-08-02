from flask import Flask, render_template, request
import pygame 
from pynput.keyboard import Key, Listener
import random 
import time as t

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route('/index')
def index():
        return render_template('home.html')

@app.route('/examination')
def examination():
        
        pygame.mixer.init()
        song_number = random.randint(1,1)
        pygame.mixer.music.load('audio_files/' + str(song_number) + '.mp3')
        pygame.mixer.music.play()
        start_time = t.time()
        while pygame.mixer.music.get_busy():
                if song_number == 1:
                        start_actual = [10.416, 62.774, 100.821, 163.337, 282.550]
                        stop_actual = [22.406, 77.271, 112.811, 177.860, 294.551]
                        start_user = []
                        stop_user = []
                        for event in pygame.event.get():
                                if(event.type==pygame.KEYDOWN):
                                        if(event.type==pygame.K_SPACE):
                                                print('spacebar pressed')
                                if(event.type==pygame.KEYUP):
                                        print('spacebar released')
                        
                if song_number == 2:
                        start_actual = [24.045, 51.677, 125.068, 1241.606, 277.445]
                        stop_actual = [38.562, 63.667, 137.057, 256.129, 289.446]
                        
                        start_user = []
                        stop_user = []
                if song_number == 3:
                        start_actual = [47.764, 103.014, 126.931, 185.108, 233.982]
                        stop_actual = [62.282, 115.003, 138.921, 197.108, 248.505  ]
                        
                        start_user = []
                        stop_user = []
                if song_number == 4:
                        print('song 4')
                if song_number == 5:
                        print('song 5')
        return "examination screen"


@app.route('/results')
def results():
    return "results screen"

if __name__ == "__main__":
    app.run(debug=True)


