from flask import Flask, render_template
from pygame import mixer, time
import random 
app = Flask(__name__)

@app.route("/")
def hello():
        return "Start Page"

@app.route('/examination')
def examination():
        
        mixer.init()
        song_number = random.randint(1,4)
        mixer.music.load('' + str(song_number) + '.mp3')
        mixer.music.play()
        
        while mixer.music.get_busy():
                time.Clock().tick(10)
                if song_number == 1:
                        print('song 1')
                if song_number == 2:
                 print('song 2')
                if song_number == 3:
                        print('song 3')
                if song_number == 4:
                        print('song 4')
                if song_number == 5:
                        print('song 5')


@app.route('/results')
def results():
    return "Results Screen"

if __name__ == "__main__":
    app.run()


