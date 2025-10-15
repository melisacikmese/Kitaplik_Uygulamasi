VERI_DOSYASI = "kitaplar.txt"
AYIRICI = "|"  


def kitaplari_yukle():
    kitaplar = []
    try:
        with open(VERI_DOSYASI, 'r', encoding='utf-8') as dosya:
            for satir in dosya:
                satir = satir.strip()
                if satir:
                    bilgiler = satir.split(AYIRICI)
                    if len(bilgiler) == 3:
                        kitaplar.append({
                            "Ad": bilgiler[0],
                            "Yazar": bilgiler[1],
                            "BasimYili": bilgiler[2]
                        })
    except FileNotFoundError:
        print(f"Uyarı: '{VERI_DOSYASI}' dosyası bulunamadı, yeni dosya oluşturulacak.")
    return kitaplar

def kitaplari_kaydet(kitaplar):
    try:
        with open(VERI_DOSYASI, 'w', encoding='utf-8') as dosya:
            for kitap in kitaplar:
                satir = f"{kitap['Ad']}{AYIRICI}{kitap['Yazar']}{AYIRICI}{kitap['BasimYili']}\n"
                dosya.write(satir)
        print("Kitaplar başarıyla dosyaya kaydedildi.")
    except Exception as e:
        print(f"Hata: Kitaplar kaydedilemedi. Hata: {e}")


def kitap_ekle(kitaplar):
    print("\n--- Yeni Kitap Ekle ---")
    ad = input("Kitabın Adı: ").strip()
    yazar = input("Yazarı: ").strip()
   
    while True:
        basim_yili = input("Basım Yılı: ").strip()
        if basim_yili.isdigit() and len(basim_yili) == 4:
            break
        else:
            print("Geçerli bir 4 haneli Basım Yılı giriniz.")

    yeni_kitap = {
        "Ad": ad,
        "Yazar": yazar,
        "BasimYili": basim_yili
    }
    
    kitaplar.append(yeni_kitap)
    print(f"'{ad}' adlı kitap başarıyla eklendi.")
    kitaplari_kaydet(kitaplar) 

def kitaplari_listele(kitaplar):
    print("\n--- Kitaplık İçeriği ---")
    if not kitaplar:
        print("Kitaplıkta kayıtlı eser bulunmamaktadır.")
        return

    print(f"{'No':<4} {'Kitap Adı':<40} {'Yazar':<25} {'Basım Yılı':<10}")
    print("-" * 80)
    
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i:<4} {kitap['Ad']:<40} {kitap['Yazar']:<25} {kitap['BasimYili']:<10}")
    print("-" * 80)

def kitap_ara(kitaplar):
    print("\n--- Kitap Ara ---")
    if not kitaplar:
        print("Kitaplıkta kayıtlı eser bulunmamaktadır.")
        return
        
    arama_terimi = input("Aramak istediğiniz kelimeyi (Kitap Adı veya Yazar) girin: ").strip().lower()
    
    if not arama_terimi:
        print("Arama terimi boş bırakılamaz.")
        return

    sonuclar = []
    for kitap in kitaplar:
        if arama_terimi in kitap['Ad'].lower() or arama_terimi in kitap['Yazar'].lower():
            sonuclar.append(kitap)

    print(f"\n--- '{arama_terimi}' için {len(sonuclar)} Sonuç ---")
    if not sonuclar:
        print("Arama kriterinize uygun kitap bulunamadı.")
    else:
        print(f"{'No':<4} {'Kitap Adı':<40} {'Yazar':<25} {'Basım Yılı':<10}")
        print("-" * 80)
        
        for i, kitap in enumerate(sonuclar, 1):
            print(f"{i:<4} {kitap['Ad']:<40} {kitap['Yazar']:<25} {kitap['BasimYili']:<10}")
        print("-" * 80)


def ana_menu():
    print("\n" + "="*40)
    print("        KİTAPLIK UYGULAMASI")
    print("="*40)
    print("1. Kitap Ekle")
    print("2. Kitapları Listele")
    print("3. Kitap Ara (Basit)")
    print("4. Çıkış ve Kaydet")
    print("="*40)
    secim = input("Seçiminizi girin (1-4): ").strip()
    return secim

def main():
    kitaplar = kitaplari_yukle() 

    while True:
        secim = ana_menu()

        if secim == '1':
            kitap_ekle(kitaplar)
        elif secim == '2':
            kitaplari_listele(kitaplar)
        elif secim == '3':
            kitap_ara(kitaplar)
        elif secim == '4':
            print("Uygulamadan çıkılıyor. Kayıtlar dosyaya yazıldı.")
            break 
        else:
            print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()