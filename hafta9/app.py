from flask import Flask,request
from flask.templating import render_template

app=Flask(__name__)

@app.route("/",methods=["get"])
def anasayfa():
    return render_template("anasayfa.html",hata="")

kullaniciAdi="admin"
sifre="1234"

@app.route("/kullanicigiriskontrol",methods=["POST"])
def girisKontrol():
    kadi=""
    r_sifre=""
    if request.method=="POST":
        print("post metoduna girildi")
        kadi=request.form.get("input_kadi")
        r_sifre=request.form.get("input_sifre")
    
    if kullaniciAdi==kadi and sifre==r_sifre:
        return render_template("hosgeldiniz.html")
    else:
        return render_template("anasayfa.html",hata="Kadi veya şifreniz hatalı")


if __name__ == "__main__":
    app.run(debug=True)