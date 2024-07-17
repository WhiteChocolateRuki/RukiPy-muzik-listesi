#21100011057
#Rukiye Uçar

import random

def ana_menu():
    print("""
#######################################   
#RukiPy  Müzik Listesine Hoş Geldinizz#
#######################################
Yapmak İstediğiniz İşlemi Seçiniz:
 1. Şarkı İşlemleri   
 2. Şarkı Sözleri İşlemleri
 3. Çıkış
    """)

def sarki_menu():
    def sarki_ana_menu():
            print("""
#######################################   
#RukiPy Müzik Listesine Hoş Geldinizz#
#######################################
Yapmak İstediğiniz İşlemi Seçiniz:
1. Şarkı Ekle
2. Şarkı Güncelle
3. Şarkı Ara
4. Şarkı Sil
5. Tüm Şarkıları Listele
6. Şarkıları Filtrele  
7. Bana Şarkı Öner
8. Akıllı Mixten Öner
9. Ana Menüye Dön
    """)

    def sarki_ekle():
        while True:
            try:
                ad=input("Şarkı Adı: ")
                sanatci=input("Sanatçı Ad: ")
                tur=input("Şarkı Türü: ")

                with open("playlist.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"Adı: {ad}, Sanatçı: {sanatci}, Türü: {tur}\n")
                
                print("_______________________")
                print("Şarkı Başarıyla Eklendi")
                break
            except:
                print("\nUPPPS! Bir Hata Oluştu. lütfen Tekrar Deneyin")
    def sarki_guncelle():
        while True:
            try:
                print("*******************************************************")
                with open("playlist.txt", "r", encoding="utf-8") as dosya:
                    liste =dosya.read()
            
                if not liste:
                    print("________________________________")
                    print("Güncellenecek şarkı bulunmamakta")
                else:
                    print(liste)
                print("*******************************************************")
            
                
                sarki_adi=input("Güncellenecek Şarkının Adını Yazın: ")
                guncel=False

                with open("playlist.txt", "r", encoding="utf-8") as dosya:
                    girdi=dosya.readlines()

                for i, satir in enumerate(girdi):
                    if sarki_adi in satir:
                        yeni_ad=input("Yeni Şarkı Adı: ")
                        yeni_sanatci=input("Yeni Sanatçı Adı: ")
                        yeni_tur=input("Yeni Şarkı Türü: ")
                        satir=f"Adı: {yeni_ad}, Sanatçı Adı: {yeni_sanatci}, Türü: {yeni_tur}\n"
                        girdi[i]= satir
                        guncel=True
                        break

                if guncel==True:
                    with open("playlist.txt", "w", encoding="utf-8") as dosya:
                        dosya.writelines(girdi)
                    
                    print("____________________________")
                    print("Şarkı Başarıyla Güncellendi.")
                else:
                    print("_________________")
                    print("Şarkı bulunamadı.")

                break
            except:
                
                print("\nUPSSS! Bir Hata Oluştu:")
                break

    def sarki_ara():
        try:
            sarki_adi=input("Aranacak Şarkının Adını Yazın: ")

            with open("playlist.txt", "r", encoding="utf-8") as dosya:
                girdi=dosya.readlines()

            guncel=False

            for satir in girdi:
                if sarki_adi in satir:
                    print(satir.strip())
                    guncel=True

            if not guncel:
                print("_________________")
                print("Şarkı Bulunamadı.")
        except:
            print("\nUPPSS! Bir Hata Oluştu:")

    def sarki_sil():
        try:
            print("*******************************************************")
            with open("playlist.txt", "r", encoding="utf-8") as dosya:
                liste =dosya.read()
        
            if not liste:
                print("________________________________")
                print("Güncellenecek şarkı bulunmamakta")
            else:
                print(liste)
            print("*******************************************************")
            
            sarki_adi=input("Silinecek Şarkının Adını Yazın: ")

            with open("playlist.txt", "r", encoding ="utf-8") as dosya:
                satirlar=dosya.readlines()

            guncel=False
            with open("playlist.txt", "w", encoding= "utf-8") as dosya:
                for satir in satirlar:
                    if sarki_adi not in satir:    #if f"Adı: {sarki_adi}" not in satir:
                        dosya.write(satir)
                    else:
                        guncel=True

            if guncel==True:
                print("________________________")
                print("Şarkı başarıyla silindi.")
            else:
                print("_________________")
                print("Şarkı bulunamadı.")
        except:
            print("\nUPPPS! Bir Hata Oluştu" )

    def sarkilari_listele():
        try:
            print("*******************************************************")
            with open("playlist.txt", "r", encoding="utf-8") as dosya:
                liste =dosya.read()
            
            if not liste:
                print("__________________")
                print("Şarkı Listesi Boş.")
            else:
                print(liste)
            print("*******************************************************")
            

        except:
            print("\nUPPSS! Bir Hata Oluştu")


    def sarkilari_filtrele():
        try:
            tur= input("Filtrelemek İstediğiniz Şarkı Türünü Yazın: ")

            with open("playlist.txt", "r", encoding= "utf-8") as dosya:
                girdi=dosya.readlines()

            filtreli_sarkilar =[]
            for satir in girdi:
                sarki_bilg=satir.split(", ")
                if sarki_bilg[2]== f"Türü: {tur}\n":
                    filtreli_sarkilar.append(sarki_bilg)

            if len(filtreli_sarkilar)==0:
                print("__________________________________")
                print("Aradığınız Türde Şarkı Bulunamadı.")
            else:
                for sarki in filtreli_sarkilar:
                    ad=sarki[0].split(": ")[1]
                    sanatci=sarki[1].split(": ")[1]
                    tur=sarki[2].split(": ")[1].strip()

                    print("_____________________________________________")
                    print(f"Adı: {ad}, Sanatçı Adı: {sanatci}, Türü: {tur}")
                    print("_____________________________________________")

        except:
            print("\nUPPSS! Bir Hata Oluştu")

    def sarki_oner():
        try:
            with open("playlist.txt", "r", encoding="utf-8") as dosya:
                girdi = dosya.readlines()

            if len(girdi) == 0:
                print("__________________")
                print("Müzik Listeniz Boş")
            else:
                oner_sarki = random.choice(girdi)
                
                print(oner_sarki)
        except:
            print("\nUPSSS! Bir hata oluştu")

    #Geçen seneki final projeme ek olarak yazdığım kod
    def akilli_mix():
        try:
            with open("akilli_mix.txt", "r", encoding="utf-8") as dosya:
                rastgele = dosya.readlines()
            
            mix = random.choice(rastgele)
            print(mix)
        except:
            print("\nUPSSS! Bir hata oluştu")

    while True:
        sarki_ana_menu()
        secim=input("Bir işlem seçin (1-9): ")

        if secim=="1":
            sarki_ekle()
            
        elif secim=="2":
            sarki_guncelle()
        elif secim=="3":
            sarki_ara()
        elif secim=="4":
            sarki_sil()
        elif secim=="5":
            sarkilari_listele()
        elif secim=="6":
            sarkilari_filtrele()
        elif secim== "7":
            sarki_oner()
        elif secim=="8":
            akilli_mix()
        elif secim=="9":
            print("__________________________________")
            print("Ana Menüye Yönlendiriliyorsunuz...")
            break
            ana_menu()    

        else:
            print("\nUPPSS! Bir Hata Oluştu. Tekrar Deneyin ")    


       
def soz_menu():
    def soz_ana_menu():
        print("""
#######################################   
#RukiPy Şarkı Sözlerine Hoş Geldinizz##
#######################################
Yapmak İstediğiniz İşlemi Seçiniz:
1) Şarkı Sözü Ekle
2) Şarkı Sozlerini Listele
3) Rastgele Şarkı Sözü
4) Akıllı Mixten Söz Öner
5) Ana Menüye Dön 
    """)


    def sarki_sozu_ekle():

        while True:

            try:
                ad= input("Şarkı Adı: ")
                sanatci=input("Sanatçı Ad: ")
                soz=input("Şarkı Sözü: ")

                with open("playlist_sozler.txt", "a", encoding="utf-8") as dosya2:
                    dosya2.write("{} - {} -> {}\n".format(ad,sanatci,soz))

                print("____________________________")
                print("Şarkı Sözü Başarıyla Eklendi")
                break
            except:
                print("\nUPPSS! Bir Hata Oluştu. Lütfen Tekrar Deneyiniz")

    def sarki_sozlerini_listele():
        try:
            print("*******************************************************")
            with open("playlist_sozler.txt", "r", encoding="utf-8") as dosya2:
                listele =dosya2.read()
            
            if  not listele:
                print("\nUPPSS! Şarkı Alıntı Listeniz Boş")
            else:
                print(listele)
            print("*******************************************************")
        except:
            print("\nUPPSS! Bir Hata Oluştu")

    def soz_oner():
        try:
            with open("playlist_sozler.txt", "r", encoding="utf-8") as dosya2:
                oner = dosya2.readlines()

            if len(oner) == 0:
                print("_________________________")
                print("Şarkı Alıntı Listeniz Boş")
            else:
                oner_soz = random.choice(oner)
                
                print(oner_soz)
        except:
            print("\nUPPPSS! Bir Hata Oluştu")
    
    #Geçen seneki final projeme ek olarak yazdığım kod
    def akilli_soz():
        try:
            with open("akilli_soz.txt", "r", encoding="utf-8") as dosya:
                rastgele = dosya.readlines()
            
            mix = random.choice(rastgele)
            print(mix)
        except:
            print("\nUPSSS! Bir hata oluştu")
    while True:
        soz_ana_menu()
        secim=input("Bir İşlem Seçin (1-5): ")
        if secim=="1":
            sarki_sozu_ekle()
        elif secim=="2":
            sarki_sozlerini_listele()
        elif secim=="3":
            soz_oner()
        elif secim == "4":
            akilli_soz()
        elif secim=="5":
            print("__________________________________")
            print("Ana Menüye Yönlendiriliyorsunuz...")
            ana_menu() 
            break
                      
        else:
            print("\nUPPSS! Bir Hata Oluştu. Tekrar Deneyin ")


while True:
    ana_menu()
    secim=input("Bir işlem seçin (1-3): ")
    if secim=="1":
        sarki_menu()

    elif secim=="2":
        soz_menu()
    elif secim=="3":
        print("\nGörüşmek Üzere Tekrar Beklerizzz:)")
        break
    else:
        print("\nUPPSS! Bir Hata Oluştu. Tekrar Deneyin ")    
