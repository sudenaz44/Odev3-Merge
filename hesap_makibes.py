def ortalama_hesapla(vize, final):
    return (vize * 0.4) + (final * 0.6)

vize = float(input("Vize notunu gir: "))
final = float(input("Final notunu gir: "))

ortalama = ortalama_hesapla(vize, final)

print(f"Ortalaman: {ortalama}")

if ortalama >= 50:
    print("Geçtin! Tebrikler 🎉")
else:
    print("Kaldın amk, seneye tekrar 😭")
    
    
        cd Masaüstü/Odev3-Merge  # klasör yolun neyse artık
git init
git remote add origin https://github.com/sudenaz44/Odev3-Merge.git
git branch -M main
git add .
git commit -m "main branch için başlangıç kodu"
git push -u origin main