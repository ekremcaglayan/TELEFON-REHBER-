import json

print("""    *************************

        REHBERE HOŞGELDİNİZ

    *************************""")
print("""
BİR İŞLEM SEÇİNİZ:
1- KİŞİ EKLE 
2- KİŞİYİ SİL
3- KİŞİLERİMİ GÖSTER
4- KİŞİNİN BİLGİLERİNİ GÖSTER
q- ÇIKIŞ

                """)


while True:    
    islem = input("Seçtiğiniz işlemi tuşlayınız : ")
    
    
    if (islem == "q"):
        print ("İşlemleriniz tamamlandı. İyi günler...")
        break
    
    
    if (islem == "1"):
        isim = input("ismi giriniz: ")
        soyad = input("soyadı giriniz: ")
        e_mail = input("e mail giriniz: ")
        telefon_numarasi = input("telefon numarası giriniz: ")

        yeni_kisi={
            isim: {
                'soyad': soyad,
                'e mail': e_mail,
                'telefon numarasi':telefon_numarasi 
            }
        }
        with open("rehber.json") as f:
            rehber = json.load(f)
            rehber["rehber"].update(yeni_kisi)
        with open("rehber.json","w") as f:
            json.dump(rehber,f)
        print("İşleminiz tamamlandı.")
    
    
    if (islem == "2"):
        print ("Silmek istediğniz kişinin adını giriniz")        
        with open("rehber.json") as f:
            rehber = json.load(f)
            kisi = input("Adı giriniz: ")
            rehber["rehber"].pop(kisi,None)
        with open("rehber.json","w") as f:  
            json.dump(rehber,f)      
        print("İşleminiz tamamlandı.")


    if (islem == "3"):
        print("Rehberinizde gösterilen isimler bulunmaktadır.")
        with open("rehber.json") as f:
            rehber = json.load(f)
            print(rehber)
        print("İşleminiz tamamlandı.")    
    
    if (islem == "4"):
        with open("rehber.json","r") as f:
            rehber = json.load(f)
            kisi = input("Kişinin ismini giriniz: ")
            print(rehber["rehber"][kisi])
        print("İşleminiz tamamlandı.")
