# kitaplik.py

DOSYA = "kitaplar.txt"

def yükle():
    kitaplar = []
    try:
        with open(DOSYA, "r", encoding="utf-8") as f:
            for satır in f:
                ad, yazar, yil = satır.strip().split("|")
                kitaplar.append({"ad": ad, "yazar": yazar, "yil": yil})
    except FileNotFoundError:
        pass
    return kitaplar

def kaydet(kitaplar):
    with open(DOSYA, "w", encoding="utf-8") as f:
        for k in kitaplar:
            f.write(f"{k['ad']}|{k['yazar']}|{k['yil']}\n")

def ekle(kitaplar):
    kitaplar.append({
        "ad": input("Kitap adı: "),
        "yazar": input("Yazar: "),
        "yil": input("Basım yılı: ")
    })
    kaydet(kitaplar)
    print("Kitap eklendi!\n")

def listele(kitaplar):
    if not kitaplar:
        print("Kayıtlı kitap yok.\n")
        return
    print("\nKitap Listesi:")
    for i, k in enumerate(kitaplar, 1):
        print(f"{i}. {k['ad']} - {k['yazar']} ({k['yil']})")
    print()

def ara(kitaplar):
    s = input("Aranan kitap adı veya yazar: ").lower()
    bulunan = [k for k in kitaplar if s in k['ad'].lower() or s in k['yazar'].lower()]
    if bulunan:
        for k in bulunan:
            print(f"{k['ad']} - {k['yazar']} ({k['yil']})")
    else:
        print("Kitap bulunamadı.\n")

def menu():
    kitaplar = yükle()
    while True:
        print("1. Kitap Ekle  2. Listele  3. Ara  4. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1": ekle(kitaplar)
        elif secim == "2": listele(kitaplar)
        elif secim == "3": ara(kitaplar)
        elif secim == "4": break
        else: print("Geçersiz seçim!\n")

if __name__ == "__main__":
    menu()