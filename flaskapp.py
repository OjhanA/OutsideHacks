
import jwcrypto
from flask import Flask, render_template
app = Flask(__name__)



@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/queue")
def hello():
    queues = [
    {
    "song" : "Despacito",
    "artist": "Luis Fonsi",
    "album": "Despacito"
    } ,
    {
    "song" : "Despacito 2",
    "artist": "Luis Fonsi",
    "album": "Despacito 2"
    } ,

]
    return render_template('queue.html', queuesList = queues)

@app.route("/stats")
def stats():
    return render_template('stats.html')

@app.route("/tag")
def tag():
    return render_template('tag.html')

def getSong():
    song = "Like Dat"
    artist = "Kodak Black"
    album = "Instituition"
    return {"song": song , "artist": artist , "album": album}

def getQueue():
    return queues


if __name__ == '__main__':
    app.run(debug=True)