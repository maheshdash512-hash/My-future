"""Our Story: a multi-page love-story site built with Flask.

Run:  pip install -r requirements.txt
      python app.py        ->  http://127.0.0.1:5000
Edit the CONTENT section below to change any text or photo.
"""
from flask import Flask, render_template

app = Flask(__name__)

# ---------- CONTENT: edit these ----------
TITLE_LINES = ("Still you.", "Always you.")

PHOTOS = [  # file = name in static/img (without .jpg); wide = landscape frame
    dict(file="cake",   wide=True,  tilt=-2, caption="Make a wish",
         alt="Birthday cake with three candles, the two of us behind it"),
    dict(file="mirror", wide=False, tilt=3,  caption="Dressed up, just because",
         alt="Mirror selfie, her arms around his shoulders"),
    dict(file="kiss",   wide=False, tilt=-3, caption="Soft light, softer kiss",
         alt="A kiss on the cheek by candlelight"),
    dict(file="temple", wide=True,  tilt=2,  caption="An evening I'd repeat",
         alt="The two of us at night in front of a temple"),
    dict(file="wood",   wide=False, tilt=-2, caption="Cheek to cheek",
         alt="Close selfie, cheek to cheek"),
]

LETTER = [
    "My love,",
    "I don't say this enough, but meeting you is one of the best things "
    "that has ever happened to me.",
    "Thank you for your patience, for the laughs, for the long talks, and "
    "for staying close on the days I'm difficult.",
    "However busy life gets, remember one thing: you will always be my "
    "favourite person.",
]
SIGNOFF = "Yours, always"

PROMISES = [
    "I will never go to bed angry.",
    "I will say the hard thing gently.",
    "I will always share the last bite.",
    "I will choose you again, every ordinary morning.",
    "I will still look at you like this when we are old.",
]
# ------------------------------------------


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=" ".join(TITLE_LINES),
        title_line1=TITLE_LINES[0],
        title_line2=TITLE_LINES[1],
        photos=PHOTOS,
        letter=LETTER,
        signoff=SIGNOFF,
        promises=PROMISES,
    )


if __name__ == "__main__":
    app.run(debug=True)
