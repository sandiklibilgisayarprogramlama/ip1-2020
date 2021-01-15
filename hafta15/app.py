from flask import Flask
from flask.globals import request
from flask.helpers import flash
from flask.templating import render_template
from werkzeug.utils import redirect, secure_filename


app=Flask(__name__)
app.secret_key="flasuıdfhaoıdj90p8ujknlyvg8hhblı78nn"
#app.config.from_pyfile("config.py")
#print(app.config['UPLOAD_FOLDER'])

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    if request.method=="POST":
        uname=request.form.get("inp_uname")
        passw=request.form.get("inp_pass")

        if uname=="admin" and passw=="admin":
            flash("Hoşgeldiniz")
            return redirect("/admin")
        else:
            flash("işlem başarısız")
            return redirect("/")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/load",methods=["GET","POST"])
def load():
    if request.method=="POST":
        f=request.files["inp_file"]
        f.save(secure_filename(f.filename))
        flash("dosya yuklendi")
        return redirect("/load")
    else:
        return render_template("dosyayukle.html")

if __name__ == "__main__":
    app.run(debug=True)