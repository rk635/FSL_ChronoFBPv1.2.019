from flask import Flask, render_template
from pygame import mixer, time
app = Flask(__name__)

@app.route("/")
def hello():
        return "Start Page"

@app.route('/examination')
def examination():
 mixer.init()
 mixer.music.load('sond.mp3')
 mixer.music.play()
 while mixer.music.get_busy():
         time.Clock().tick(10)
 return "Examination Screen"



@app.route('/results')
def results():
    return "Results Screen"

if __name__ == "__main__":
    app.run()


