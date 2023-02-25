import os
import json
from markupsafe import escape
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/about.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", about_data=data)


@app.route("/personas")
def personas():
    data = []
    with open("data/personas.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("personas.html", page_title="The Personas", personas=data)

@app.route("/persona/<persona_name>")
def about_persona(persona_name):
    persona = {}
    with open("data/personas.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == persona_name:
                persona = obj
    return render_template("member.html", persona=persona)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)