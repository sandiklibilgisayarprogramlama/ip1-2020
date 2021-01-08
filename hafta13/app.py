from flask import Flask
from flask.globals import request
from flask.templating import render_template
from werkzeug.exceptions import abort
from werkzeug.utils import redirect


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def anasayfa():
    if request.method=="POST":
        name=request.form.get("inp_name")
        if name=="admin":
            return redirect("/hosgeldin")
        else:
            abort(401)
    else:
        return render_template("anasayfa.html")

@app.route("/hosgeldin")
def hosgeldin():
    return "hoşgeldin"


if __name__ == "__main__":
    app.run(debug=True)