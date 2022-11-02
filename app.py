import flask
import random

app = flask.Flask(__name__) #like psvm for flask apps

possible_images = [
    "/static/bats.jpg",
    "/static/ghostie.webp",
    "/static/Horse_and_Man.jpg",
]
#if hitting internal server error, its a python bug
@app.route("/")
def index():
    img = random.choice(possible_images)
    return flask.render_template(
        "index.html",
        spooky_image = img, #passing this into the html, remember to use {{}}
    )

@app.route("/pumpkin_patch") #whatever the path is, put it here
def pumpkin_patch():
    return flask.render_template("pumpkin_patch.html")

app.run()
