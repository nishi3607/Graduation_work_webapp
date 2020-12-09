# Flaskとrender_templateをインポート
from flask import Flask, render_template
import requests
from flask import Flask
from flask import request

# Flaskオブジェクトの作成

app = Flask(__name__)


# [/]にアクセスがあった
@app.route("/")
def inde():
    return "<h1>/index?name=名前を入れてね</p1>"


@app.route("/index")
def index():
    name = request.args.get("name")
    study = ['python', 'SQL', 'WebAPI', 'Git']
    return render_template("index_1.html", name=name, study=study)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    study = ['python', 'SQL', 'WebAPI', 'Git']
    return render_template("index_1.html", name=name, study=study)


if __name__ == "__main__":
    app.run(debug=True)
