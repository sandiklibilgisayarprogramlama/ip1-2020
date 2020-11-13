from flask import Flask

app = Flask(__name__)

@app.route("/topla/<x>/<y>")
def top(x,y):
    return "toplam : "+str(float(x)+float(y))

@app.route("/cikar/<x>/<y>")
def cik(x,y):
    return "fark : "+str(float(x)-float(y))

@app.route("/carp/<x>/<y>")
def carp(x,y):
    return "çarpım : "+str(float(x)*float(y))

@app.route("/bol/<x>/<y>")
def bol(x,y):
    return "bölüm : "+str(float(x)/float(y))

@app.route("/mod/<x>/<y>")
def mod(x,y):
    return "mod : "+str(float(x)%float(y))

if __name__ == "__main__":
    app.run(debug=True)