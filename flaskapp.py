
import jwcrypto
from flask import Flask, render_template
app = Flask(__name__)

queues = [
    {
    "song" : "Despacito",
    "artist": "Luis Fonsi",
    "album": "Despacito"
    }
]

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/queue")
def hello():
    # for x in range(1):
    #     queues[x] = getSong()
    return render_template('queue.html')

@app.route("/stats")
def stats():
    return render_template('stats.html')

def getSong():
    song = "Like Dat"
    artist = "Kodak Black"
    album = "Instituition"
    return {"song": song , "artist": artist , "album": album}


if __name__ == '__main__':
    app.run(debug=True)