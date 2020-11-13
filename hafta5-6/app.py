from araba import Araba
from flask import Flask
from flask.templating import render_template

app=Flask(__name__)

mercedes=Araba()
mercedes.id="merdeces"
mercedes.beygir=70
mercedes.icerik="güzel araba"
mercedes.model=2015
mercedes.renk="Siyah"
mercedes.resimyolu="mercedes.jpg"
mercedes.marka="Mercedes Benz"

audi=Araba()
audi.id="audi"
audi.beygir=90
audi.icerik="güzel araba"
audi.model=2013
audi.renk="Beyaz"
audi.resimyolu="audi.png"
audi.marka="Audi A3"

ford=Araba()
ford.id="ford"
ford.beygir=90
ford.icerik="güzel araba"
ford.model=2019
ford.renk="Beyaz"
ford.resimyolu="ford.png"
ford.marka="Ford Focus"

opel=Araba()
opel.id="opel"
opel.beygir=80
opel.icerik="güzel araba"
opel.model=2004
opel.renk="Kırmızı"
opel.resimyolu="opel.png"
opel.marka="Opel Astra"

@app.route("/")
def anasayfa():
    return render_template("index.html", araclar=[mercedes, audi, ford, opel])

@app.route("/detay/<x>")
def detay(x):
    arabalar=[mercedes,audi,ford,opel]
    gosterilecek=None
    for araba in arabalar:
        if araba.id==x:
            gosterilecek=araba
            break
    
    return render_template("detay.html",garaba=gosterilecek)



if __name__ == "__main__":
    app.run(debug=True)