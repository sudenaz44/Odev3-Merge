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