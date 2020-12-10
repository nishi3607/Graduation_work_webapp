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
    teacher_name = []
    name = request.get("name")
    if name == ["大平", "伊藤"]:
        teacher_name = '先生'

    return render_template("index_1.html", name=name,teacher_name=teacher_name)


@app.route("/index", methods=["post"])
def post():
    teacher_name = []
    name = request.form["name"]
    if name == ["大平","伊藤"]:
        teacher_name = '先生'
    return render_template("index_1.html", name=name,teacher_name=teacher_name)


if __name__ == "__main__":
    app.run(debug=True)
