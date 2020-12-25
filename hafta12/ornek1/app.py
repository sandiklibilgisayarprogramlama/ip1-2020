from flask import Flask
from flask.globals import request
from flask.templating import render_template
from werkzeug.utils import redirect

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def anasayfa():
    if request.method=="POST":
        inp=request.form.get("inp_text")
        if inp=="yönetici":
            return redirect("/yonetici/ahmet")
            #redirect ile rotaya url parametreside gönderilebilir.
        elif inp=="kullanici":
            return redirect("/kullanici")
        else:
            return "Hatalı giriş yaptınız"
    else:
        return render_template("index.html")

@app.route("/yonetici/<ad>")
def sayfa2(ad):
    return render_template("yonetici.html",veri=ad)

@app.route("/kullanici")
def sayfa3():
    return render_template("kullanici.html")

if __name__ == "__main__":
    app.run(debug=True)