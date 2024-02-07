import random
import time
import math
class bilgisayar():
    def __init__(self,pcdurumu = "Kapalı",işletimsistemi = ["Windows 10"],model = "Dell G3 15",uygulamalar = ["Google Chrome","Opera","The Witcher 3:WildHunt"]):
        self.işletimsistemi = işletimsistemi
        self.model = model
        self.pcdurumu = pcdurumu
        self.uygulamalar = uygulamalar
 
    def açma(self):
        if self.pcdurumu == "Kapalı":
            print("Bilgisayar Açılıyor...")
            time.sleep(1)
            self.pcdurumu = "Açık"
            print("Bilgisayar Açıldı.")
        elif self.pcdurumu == "Açık":
            print("Bilgisayar Zaten Açık.")
    def kapama(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            print("Bilgisayar Kapatılıyor...")
            time.sleep(1)
            self.pcdurumu = "Kapalı"
            print("Bilgisayar Kapandı.")
        elif self.pcdurumu == "Kapalı":
            print("Bilgisayar Zaten Kapalı.")
    def hesapmakinesi(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            print("""****************************************
            HESAP MAKİNESİv2.5
            ****************************************
            İŞLEMLER
            ****************************************
            1 = TOPLAMA
            2 = ÇIKARMA
            3 = ÇARPMA
            4 = BÖLME
            5 = FAKTÖRİYEL ALMA
            6 = ÜS ALMA
            7 = KAREKÖK BULMA
            ****************************************""")
            işlem = input("İşlem Giriniz:")
            toplama = 0
            if işlem == "1":
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayılar Toplamı={}".format(sayi1+sayi2))
            elif işlem == "2":
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayılar Farkı={}".format(sayi1-sayi2))
            elif işlem == "3":
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayılar Çarpmı={}".format(sayi1*sayi2))
            elif işlem == "4":
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayılar Bölümü={}".format(sayi1/sayi2))
            elif işlem == "5":
                sayi1 = int(input("Sayı Giriniz:"))
                print("{} Sayısının Faktoriyeli = {}".format(sayi1,math.factorial(sayi1)))
            elif işlem == "6":
                sayi1 = int(input("Sayı Giriniz:"))
                üs = int(input("Alınacak Üssü Giriniz:"))
                print("{} Sayısının Karesi = {}".format(sayi1,sayi1 ** üs))
            elif işlem == "7":
                sayi1 = int(input("Sayı Giriniz:"))
                sağlama = sayi1 ** 0.5
                print("Sayının Karekökü:{}".format(sağlama))
            else:
                print("Geçersiz İşlem Girildi!")
        elif self.pcdurumu == "Kapalı" or self.pcdurumu == "kapalı":
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
    def sayıtahminoyunu(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            print("Oyunun Başlaması İçin İlk Önce 2 Sayı Girerek Sayı Aralığını Belirtiniz!")
            sayi1 = int(input("İlk Sayıyı Giriniz:"))
            sayi2 = int(input("İkinci Sayıyı Giriniz:"))
            print("Sayı Aralığımız:{}-{}".format(sayi1,sayi2))
            print("Rastgele Sayı Seçiliyor...")
            rastgele_sayi = random.randint(sayi1,sayi2)
            print("Sayı Seçildi İyi Şanslar İhtiyacınız Olacak :))")
            print("----------5 Tahmin Hakkı Verildi----------")
            while True:
                hak = 5
                tahmin = int(input("Tahmininizi Giriniz:"))
                if tahmin < rastgele_sayi:
                    print("Yanlış Tahmin :)")
                    print("Bence Daha Büyük Bir Sayı Yazmanız Haklarınız Korumanıza Yardımcı Olacaktır:)")
                    hak -= 1
                    print("Kalan Hakkınız:{}".format(hak))
                elif tahmin > rastgele_sayi:
                    print("Yanlış Tahmin Bu İşte Yenisiniz Sanırım :)")
                    print("Sizce de Sayı Fazla Büyük Değil Mi ?")
                    hak -= 1
                    print("Kalan Hakkınız:{}".format(hak))
                elif tahmin == rastgele_sayi:
                    print("Doğru Tahmin!!")
                    print("Talimatlarımla Başardınız Efendim :)")
                    break
                elif hak == 1:
                    print("Son Hakkınız Kaldı Biraz Dikkatli Olun Derim :) ")
                elif hak == 2:
                    print("Dikkatli Olun Demiştim Hakkınız Kalmadı :)))")
                    print("Oyun Kapatılıyor...")
                    time.sleep(1)
                    print("Oyun Kapatıldı")
                    break
        elif self.pcdurumu == "Kapalı" or self.pcdurumu == "kapalı":
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
    def __len__(self):
        return len(self.işletimsistemi)
    def __str__(self):
        return """---------------------------
        Bilgisayar Özellikleri
        ---------------------------
        Model:{}
        İşletim Sistemi:{}
        Pc Durumu:{}
        Uygulama Listesi{}
        ---------------------------""".format(self.model,self.işletimsistemi,self.pcdurumu,self.uygulamalar)
 
    def işletim_sistemi_kaldır(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            if len(self.işletimsistemi) == 1:
                print("Mevcut İşletim Sistemi = {}".format(self.işletimsistemi[0]))
                işlem = input("İşletim Sisteminizi Kaldırmak İstiyor musunuz?:")
                if işlem == "Evet" or işlem == "evet":
                    print("{} Kaldırılıyor Lütfen Bekleyiniz...".format(self.işletimsistemi[0]))
                    time.sleep(2)
                    self.işletimsistemi.pop(0)
                    print("Mevcut İşletim Sisteminiz Kaldırıldı Yeni Bir İşletim Sistemi İçin 'İşletim Sistemi Yükle' Seçeneğini Seçebilirsiniz.")
                elif işlem == "Hayır" or işlem == "hayır":
                    print("Çıkış Yapılıyor...")
                    time.sleep(1)
                    print("Çıkış Yapıldı.")
                else:
                    print("Geçersiz İşlem Girdiniz")
            else:
                print("Bilgisayar İşletim Sistemine Herhangi Bir İşletim Sistemine Sahip Değil")
        elif self.pcdurumu == "Kapalı" or self.pcdurumu == "kapalı":
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
    def işletim_sistemi_yükle(self):
        if self.pcdurumu == "açık" or self.pcdurumu == "Açık":
            if self.işletimsistemi == list():
                seçim = input("İşletim Sisteminiz Bulunmamakta Bir Tane Edinmek İster misiniz?:")
                if seçim == "Evet" or seçim == "evet":
                    işletimsistemleri = ["Mac","Windows 10","SteamOS","Linux"]
                    print("Yüklenebilecek İşletim Sistemleri:")
                    sayac = 0
                    for i in işletimsistemleri:
                        print("Numara:{}|İşletim Sistemi:{}".format(sayac,i))
                        sayac += 1
                    işlem = input("Lütfen Yüklenmesini İstediğiniz İşletim Sisteminin Numarasını Giriniz:")
                    if işlem == "0":
                        print("{} Yükleniyor Lütfen Bekleyiniz...".format(işletimsistemleri[0]))
                        time.sleep(2)
                        self.işletimsistemi.append("Mac")
                        print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletimsistemleri[0],self.işletimsistemi[0]))
                    if işlem == "1":
                        print("{} Yükleniyor Lütfen Bekleyiniz...".format(işletimsistemleri[1]))
                        time.sleep(2)
                        self.işletimsistemi.append("Windows 10")
                        print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletimsistemleri[1],self.işletimsistemi[0]))
                    if işlem == "2":
                        print("{} Yükleniyor Lütfen Bekleyiniz...".format(işletimsistemleri[2]))
                        time.sleep(2)
                        self.işletimsistemi.append("SteamOS")
                        print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletimsistemleri[2],self.işletimsistemi[0]))
                    if işlem == "3":
                        print("{} Yükleniyor Lütfen Bekleyiniz...".format(işletimsistemleri[3]))
                        time.sleep(2)
                        self.işletimsistemi.append("Linux")
                        print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletimsistemleri[3],self.işletimsistemi[0]))
            elif len(self.işletimsistemi) > 0:
                print("Zaten Bir İşletim Sisteminiz Bulunmakta Yenisini Kurmak İçin Mevcut Olanı Kaldırmanız Gerek")
                print("Programdan Çıkış Yapılıyor...")
                time.sleep(1)
                print("Çıkış Yapıldı.")
        elif self.pcdurumu == "Kapalı" or self.pcdurumu == "kapalı":
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
 
    def bilgilerigöster(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            print("---------------------------\nBilgisayar Özellikleri\n---------------------------\nModel:{}\nİşletim Sistemi:{}\nPc Durumu:{}\nUygulama Listesi{}\n---------------------------".format(self.model,self.işletimsistemi,self.pcdurumu,self.uygulamalar))
        elif self.pcdurumu == "Kapalı" or self.pcdurumu == "kapalı":
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
bilgisayar = bilgisayar()
print("""-----------------------------------------
    Bilgisayar İşlemleri
    -----------------------------------------
    1 = AÇMA
    2 = KAPAMA
    3 = HESAP MAKİNESİ
    4 = BİLGİLER
    5 = İŞLETİM SİSTEMİ  KALDIR
    6 = İŞLETİM SİSTEMİ YÜKLE
    7 = SAYI TAHMİN OYUNU
    -----------------------------------------""")
while True:
    karar = input("İşlem Giriniz:")
    if karar == "1":
        bilgisayar.açma()
    elif karar == "2":
        bilgisayar.kapama()
    elif karar == "3":
        bilgisayar.hesapmakinesi()
    elif karar == "4":
        bilgisayar.bilgilerigöster()
    elif karar == "5":
        bilgisayar.işletim_sistemi_kaldır()
    elif karar == "6":
        bilgisayar.işletim_sistemi_yükle()
    elif karar == "7":
        bilgisayar.sayıtahminoyunu()
    elif karar == "q":
        print("Bilgisayar Durduruluyor...")
        break
    else:
        print("Geçersiz İşlem Girildi")
        