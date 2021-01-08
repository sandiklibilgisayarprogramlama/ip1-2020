from flask import Flask
from flask.globals import request
from flask.helpers import make_response
from flask.templating import render_template
from flask.wrappers import Response

app=Flask(__name__)


@app.route("/",methods=["POST","GET"])
def anasayfa():
    if request.method=="POST":
        name=request.form.get("inp_user")
        
        response = make_response(render_template("hosgeldin.html",isim=name))
        response.set_cookie("user",name)
        return response
    else:
        cookie = request.cookies.get("user")
        if cookie:
            return render_template("hosgeldin.html",isim=cookie)
        else:
            return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)