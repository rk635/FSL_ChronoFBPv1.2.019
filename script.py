from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

@app.route('/examination')
def examination():
    return "Examination Screen"
    
@app.route('/results')
def results():
    return "Results Screen"

if __name__ == "__main__":
    app.run()


