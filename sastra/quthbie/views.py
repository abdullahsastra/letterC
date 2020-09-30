from django.shortcuts import render,redirect
import sqlite3
from django.views.decorators.csrf import csrf_protect

def satuIndex(request):
    #db=sqlite3.connect('satu.db')
    return render(request,'login.html')

def loginIndex(request):
    if request.method == "POST":
        nom = request.POST['formemail']
        nam = request.POST['formpassword']
        db = sqlite3.connect('login.db')
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM pengguna WHERE email='"+nom+"' AND password='"+nam+"' ")
        berapa=cur.fetchone()[0]
        if berapa == 0:
            return render(request,'salah.html')
        else:
            return render(request,'index.html')
