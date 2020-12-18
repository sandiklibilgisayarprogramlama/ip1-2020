from flask import Flask
from flask.globals import request
from flask.templating import render_template
from werkzeug.utils import redirect
import uuid
from yazi import Yazi

app=Flask(__name__)

def dosyayaKaydet(id,baslik,icerik,etiket,saat):
    with open("veriler.txt","a") as f:
        f.write(str(id)+"|"+baslik+"|"+icerik+"|"+etiket+"|"+saat+"\n")
        f.close()

def dosyadanOku():
    yaziListe=[]
    with open("veriler.txt","r") as f:
        yaziListe=f.readlines()
        f.close()
    
    sayfaGosterilecekList=[]

    for satir in yaziListe:
        satir=satir.replace("\n","")
        yazi = satir.split("|")
        sayfaGosterilecekList.append(dosyayiSinifaAktar(yazi))

    return sayfaGosterilecekList

def dosyayiSinifaAktar(liste):
    return Yazi(liste[0],liste[1],liste[2],liste[3],yayintarihi=liste[4])

@app.route("/")
def anasayfa():
    liste=dosyadanOku()
    return render_template("anasayfa.html",sayfayazilistesi=liste)

@app.route("/yaziekle",methods=["POST","GET"])
def yaziEkle():
    if request.method=="POST":
        id=uuid.uuid1()
        baslik=request.form.get("inp_baslik")
        icerik=request.form.get("text_icerik")
        etiket=request.form.get("inp_etiket")
        saat=request.form.get("inp_tarih")
        dosyayaKaydet(id,baslik,icerik,etiket,saat)
        return redirect("/")
    else:
        return render_template("yaziekle.html")

@app.route("/detay/<id>")
def detay(id):
    gosterilecekYazi=None
    yaziListe=dosyadanOku()
    for yazi in yaziListe:
        if yazi.id == id:
            gosterilecekYazi=yazi
            break
    return render_template("detay.html",yaziDetay=gosterilecekYazi)


if __name__ == "__main__":
    app.run(debug=True)