from os import error
from flask import Flask
from flask.globals import request, session
from flask.templating import render_template
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app=Flask(__name__)
app.secret_key="dno3ır8yhowfn4ş9uıbnyoG!nfo9uwhneofı342"
userCredientals={"username":"ahmet","password":"123"}

@app.route("/",methods=["POST","GET"])
def anasayfa():
    if request.method=="POST":
        uname = request.form.get("inp_username")
        passw= request.form.get("inp_pass")

        if uname== userCredientals["username"] and passw == userCredientals["password"]:
            session["username"]=uname
            return redirect("/hosgeldin")
        else:
            return render_template("index.html",error="Kullanıcı adı veya şifre yanlış")
    else:
        return render_template("index.html")

@app.route("/hosgeldin")
def hosgeldin():
    if "username" in session:
        return render_template("hosgeldiniz.html",name=session["username"])
    else:
        abort(403)

@app.route("/cikisyap")
def cikisyap():
    del session["username"]
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)