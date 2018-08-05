
import jwcrypto
from flask import Flask, render_template
app = Flask(__name__)

queue = [
    {
    "song" : "Despacito",
    "artist": "Luis Fonsi",
    "album": "Despacito"
    }
]

@app.route("/")
def hello():
    for x in range(1):
        queue[x] = getSong()
    return render_template('Test.html', queue = queue)

def getSong():
    song = "Like Dat"
    artist = "Kodak Black"
    album = "Instituition"
    return {"song": song , "artist": artist , "album": album}


if __name__ == '__main__':
    app.run(debug=True)