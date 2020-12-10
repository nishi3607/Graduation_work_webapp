# Flaskとrender_templateをインポート
from flask import Flask, render_template
import requests
from flask import Flask
from flask import request

# Flaskオブジェクトの作成

app = Flask(__name__)


# [/]にアクセスがあった
@app.route("/")



@app.route("/index")
def index():
    name = request.args.get("name")
    return render_template("index_1.html", name=name)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    return render_template("index_1.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
