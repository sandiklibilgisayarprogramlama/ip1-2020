from flask import Flask,render_template

app = Flask(__name__)

liste=["bilgisauar yazısı","telefon yazısı","araba yazısı"]

@app.route("/")
def anasayfa():
    return render_template("tema.html",sayfabasligi="Anasayfa",icerik = liste)

@app.route("/hakkinda")
def hakkinda():
    return render_template("tema.html",sayfabasligi="Hakkında",icerik = "burası hakkında sayfası")


@app.route("/iletisim")
def iletisim():
    return render_template("tema.html",sayfabasligi="İletişim",icerik = "burası iletisim sayfası")

@app.route("/yazi")
def yazi():
    return render_template("tema.html",sayfabasligi="bilgisayar nedir?",icerik = "bilgisayar hesap yapabilecek bir cihazdır.")




if __name__ == "__main__":
    app.run(debug=True)