from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

@app.route("/hakkinda")
def hakkinda():
    return render_template("hakkinda.html")


if __name__ == "__main__":
    app.run(debug=True)