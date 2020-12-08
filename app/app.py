# Flaskとrender_templateをインポート
from flask import Flask, render_template

# Flaskオブジェクトの作成

app = Flask(__name__)


# [/]にアクセスがあった場合に"HELLO WORLD"の文字列を返す
@app.route("/")
def hello():
    return "卒業制作アプリだぜええええええ"


@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
