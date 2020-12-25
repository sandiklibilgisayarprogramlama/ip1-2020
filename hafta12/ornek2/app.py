from kullanici import Kullanici
from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)


kull_1=Kullanici("ahmet","uzun","yonetici")
kull_2=Kullanici("veli","yılmaz","kullanici")
kull_3=Kullanici("necmi","tatlı","kullanici")
kull_4=Kullanici("şükrü","kısa","kullanici")
sistem_kul_list=[kull_1,kull_2,kull_3,kull_4]

@app.route("/",methods=["POST","GET"])
def anasayfa():
    if request.method=="POST":
        ad=request.form.get("inp_ad")
        soyad=request.form.get("inp_soyad")
        for kul in sistem_kul_list:
            if kul.ad==ad and kul.soyad==soyad:
                return redirect(url_for("kullanicigiris",ad=kul.ad,soyad=kul.soyad,tip=kul.tip))
        
        return "sistemde böyle bir kişi tanımı yok"
    else:
        return render_template("index.html")

@app.route("/login/<ad>/<soyad>/<tip>")
def kullanicigiris(ad,soyad,tip):
    return render_template("sayfa.html",girisAd=ad,girisSoyad=soyad,girisTip=tip)

if __name__ == "__main__":
    app.run(debug=True)