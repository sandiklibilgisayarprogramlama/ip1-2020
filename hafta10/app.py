from flask import Flask
from flask.globals import request
from flask.templating import render_template
from werkzeug.utils import redirect

app=Flask(__name__)

def dosyayaKaydet(baslik,icerik,etiket,saat):
    with open("veriler.txt","a") as f:
        f.write(baslik+"|"+icerik+"|"+etiket+"|"+saat+"\n")
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
        sayfaGosterilecekList.append(yazi[0])

    return sayfaGosterilecekList
    
@app.route("/")
def anasayfa():
    liste=dosyadanOku()
    return render_template("anasayfa.html",sayfayazilistesi=liste)

@app.route("/yaziekle",methods=["POST","GET"])
def yaziEkle():
    if request.method=="POST":
        baslik=request.form.get("inp_baslik")
        icerik=request.form.get("text_icerik")
        etiket=request.form.get("inp_etiket")
        saat=request.form.get("inp_tarih")
        dosyayaKaydet(baslik,icerik,etiket,saat)
        return redirect("/")
    else:
        return render_template("yaziekle.html")


if __name__ == "__main__":
    app.run(debug=True)