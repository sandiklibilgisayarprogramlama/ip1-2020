from flask import Flask

app=Flask(__name__)


@app.route("/")
def anasayfa():
    return "merhaba"

@app.route("/hakkinda")
def hakkinda():
    return "hakkinda sayfası"



if __name__ == "__main__":
    app.run(debug=True)