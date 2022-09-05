import os 

class musteri():
    def __init__(self,name,surname,password,iban,bakiye):
        self.name = name 
        self.password = password
        self.iban = iban
        self.bakiye = bakiye
        self.surname = surname



eren = musteri("Eren","Alkış","44Eren44","12345678",2000)
yağmur = musteri("Yağmur","Alkış","44Yağmur44","2123456",2000)
musteri_list = [eren,yağmur]



def eft(alan_iban,ad,soyad,mebla):
    for kullanici in musteri_list:
        if alan_iban in kullanici.iban and ad in kullanici.name and soyad in kullanici.surname:
            kullanici.bakiye += mebla
        if alan_iban not in kullanici.iban or ad not in kullanici.name or soyad not in kullanici.surname:
            print("Bilgileri kontrol edin ")



def banner():
    print(os.system("clear && figlet EREN BANK"))
    print("Merhabalar bankamıza hoş geldiniz lütfen Adınızı ve Şifrenizi girerek giriş tuşuna basınız. Çıkış yapmak için 0'ı tuşlayınız")


def ana_menü():
    print(os.system("clear && figlet EREN BANK"))
    
    print("""
    
    [1] Para Çek
    [2] Para Yatır
    [3] Bakiye Sorgula
    [4] Eft Yap
    
    """)
    
while True:
    giris=int(input(("Giriş sayfasına gitnek için 1'i çıkış yapmak için 2'yi tuşlayın")))
    if giris==1:
        banner()
    if giris == 2:
        break
        
    
    
    kullanıcı_adı_girisi = input("Giriş yapmak için Lütfen adınızı giriniz: ")
    sifre_girisi = input("Şifrenizi giriniz: ")
    
    for ii in musteri_list:
        if kullanıcı_adı_girisi not in ii.name or sifre_girisi not in ii.password:
            print("kullanici adı veya şifre hatalı lütfen tekrar deneyin")
            continue
    
    
    for kullanici in musteri_list:
        if kullanıcı_adı_girisi in kullanici.name and sifre_girisi in kullanici.password:
            
            
            while True:
                ana_menü()
                secim = int(input("Lütfen bir işlem seçin: "))
                if secim == 1:
                    mebla = int(input("Çekmek istediğiniz meblayı giriniz: "))
                    kullanici.bakiye -= mebla
                    print(f"Güncel bakiyeniz {kullanici.bakiye}")
                    secim = int(input("Ana menüye dönmek için 1'i Çıkış yapmak için 2'yi tuşlayınız")) 
                    if secim == 1:
                        continue
                    if secim == 2:
                        break
                if secim == 2:
   
                    mebla = int(input("Yatırmak istediğiniz meblayı girin: "))
                    kullanici.bakiye += mebla
                    print(f"Güncel bakiyeniz {kullanici.bakiye}")
                    secim = int(input("Ana menüye dönmek için 1'i Çıkış yapmak için 2'yi tuşlayınız: "))
                    if secim == 1:
                        continue
                    if secim == 2:
                        break
                
                if secim == 3:
                    print(f"Güncel bakiyeniz {kullanici.bakiye}")
                    secim = int(input("Ana menüye dönmek için 1'i Çıkış yapmak için 2'yi tuşlayınız"))
                    if secim == 1:
                        continue
                    if secim == 2:
                        break
                if secim == 4:
                    alan_iban = input("Para gönderilicek İbanı giriniz: ")
                    ad = input("Para gönderilicek kişinin adı: ")
                    soyad = input("Para gönderilicek kişinin soyadı: ")
                    mebla = int(input("Göndereceğiniz meblayı girin: "))
                    eft(alan_iban,ad,soyad,mebla)
                    kullanici.bakiye -= mebla
                    print(f"Güncel bakiyeniz {kullanici.bakiye}")
                    
                    secim = int(input("Ana menüye dönmek için 1'i Çıkış yapmak için 2'yi tuşlayınız: "))
                    if secim == 1:
                        continue
                    if secim == 2:
                        break
                    







