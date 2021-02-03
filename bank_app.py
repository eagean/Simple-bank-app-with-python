from tinydb import TinyDB, Query
import random

def balancecheck(tcno):
    balancechecked = db.get(User.tcno == tcno)
    balancechecked = balancechecked.get('balance')
    return balancechecked


        
def paracekme(tcno):
    bakiye = balancecheck(tcno)
    print("Mevcut bakiyeniz = " + bakiye)
    cekilecek = input("Lütfen çekmek istediğiniz miktarı giriniz.\nÇıkış için 'iptal' yazınız.\n")
    if cekilecek.lower() == "iptal":
        islemsecici(tcno)
    else:
        try:
            int(cekilecek)
            if int(cekilecek) <= int(bakiye) and int(cekilecek) > 0:
                yeni_bakiye = int(bakiye) - int(cekilecek)
                db.update({'balance': str(yeni_bakiye)}, User.tcno == tcno)
                print("İşlem başarılı.\nHesabınızdan "+ cekilecek + "tl çektiniz. Yeni bakiyeniz: "+ str(yeni_bakiye))
                islemsecici(tcno)
            else:
                print("İşleminizi gerçekleştiremiyoruz. Lütfen tekrar deneyiniz!\n")
                paracekme(tcno)            
        except ValueError:
            print("Lütfen sadece tam sayı giriniz.\n")
            paracekme(tcno)
        

def parayatirma(tcno):
    bakiye = balancecheck(tcno)
    print("Mevcut bakiyeniz = " + bakiye)
    yatirilacak = input("Lütfen yatırmak istediğiniz miktarı giriniz.\nÇıkış için 'iptal' yazınız.\n")
    if yatirilacak.lower() == "iptal":
        islemsecici(tcno)
    else:
        try:
            int(yatirilacak)
            if int(yatirilacak) > 0:
                yeni_bakiye = int(bakiye) + int(yatirilacak)
                db.update({'balance': str(yeni_bakiye)}, User.tcno == tcno)
                print("İşlem başarılı.\nHesabınıza "+ yatirilacak + "tl yatırdınız. Yeni bakiyeniz: "+ str(yeni_bakiye))
                islemsecici(tcno)
            else:
                print("İşleminizi gerçekleştiremiyoruz. Lütfen tekrar deneyiniz!\n")
                parayatirma(tcno)        
        except ValueError:
            print("Lütfen sadece tam sayı giriniz.\n")
            parayatirma(tcno)
    
def paragonderme(tcno):
    bakiye = balancecheck(tcno)
    print("Mevcut bakiyeniz = " + bakiye)
    yatirilacak = input("Lütfen göndermek istediğiniz miktarı giriniz.\nÇıkış için 'iptal' yazınız.\n")
    if yatirilacak.lower() == "iptal":
        islemsecici(tcno)
    else:
        try:
            int(yatirilacak)
            if int(bakiye)> int(yatirilacak) and int(yatirilacak)>0:
                alici_tc = input ("Lütfen göndermek istediğiniz kişinin tc numarasını giriniz\n")
                if len(alici_tc)==11:
                    try:
                        int(alici_tc)
                        alici_tc = str(alici_tc)
                        control = db.search(User.tcno == alici_tc)   
                        if control ==[]:  
                            print("Sistemde bu tc numarası bulunamadı.\n")
                            paragonderme(tcno)
                        else:
                            control = db.get(User.tcno == alici_tc)
                            alici_isim = control.get('isim')
                            alici_bakiye = control.get('balance')##
                            onay = input(alici_isim + " adlı kullanıcıya "+ yatirilacak + " tl gönderiyi onaylıyor musunuz? evet/hayır\n")
                            if onay.lower() == "evet":
                                 yeni_bakiye = int(bakiye) - int(yatirilacak)
                                 db.update({'balance': str(yeni_bakiye)}, User.tcno == tcno)
                                 control = db.search(User.tcno == alici_tc)
                                 control = db.get(User.tcno == alici_tc)
                                 alici_bakiye = control.get('balance')
                                 alici_bakiye = int(alici_bakiye) + int(yatirilacak)
                                 db.update({'balance': str(alici_bakiye)}, User.tcno == alici_tc)
                                 print("İşlem başarılı.\n")
                                 islemsecici(tcno)
                            else:
                                print("İşleminiz iptal edilmiştir.\n")
                                islemsecici(tcno)
                    except ValueError:
                        print("Lütfen geçerli 11 karakterlik tc numarasını giriniz.\n")
                        paragonderme(tcno)
                else:
                    print("Lütfen 11 karakterlik tc numarasını giriniz.\n")
                    paragonderme(tcno)                      
            else:
                print("İşleminizi gerçekleştiremiyoruz. Lütfen tekrar deneyiniz!\n")
                islemsecici(tcno)
        except ValueError:
            print("Lütfen sadece tam sayı giriniz.\n")
            paragonderme(tcno)
            
def fatura(tcno):
    bakiye = balancecheck(tcno)
    print("Mevcut bakiyeniz = " + bakiye)
    secim = input("Lütfen yatırmak istediğiniz faturanın numarasını seçiniz.\n1 - Elektrik\n2 - Su\n3 - Doğalgaz\nÇıkış için 'iptal' yazınız.\n")
    if secim == "iptal":
        islemsecici(tcno)
    else:
        if secim == "1":
             fatura_tur = "Elektrik"
        elif secim == "2":
            fatura_tur = "Su"
        elif secim == "3":
            fatura_tur = "Doğalgaz"
        else:
            print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.\n")
            fatura(tcno)
        faturaode(tcno,fatura_tur)  

def faturaode(tcno,fatura_tur):
    bakiye=balancecheck(tcno)
    if int(bakiye) > 202:
        rastgele_tutar = random.randrange(10,201)
    else:
        rastgele_tutar = random.randrange(1,int(bakiye)+1)
    onay = input(str(rastgele_tutar) + " tl tutarındaki " + fatura_tur + " faturanızı ödemeyi onaylıyor musunuz? evet/hayır\n")    
    if onay.lower() == "evet":
         yeni_bakiye = int(bakiye) - int(rastgele_tutar)
         db.update({'balance': str(yeni_bakiye)}, User.tcno == tcno)
         print("Faturanız başarıyla yatırıldı.\n")
         islemsecici(tcno)
    else:
        print("İşleminiz iptal edilmiştir.\n")
        islemsecici(tcno)   


          
def islemsecici(tcno):
    balance = balancecheck(tcno)
    print("Mevcut Bakiyeniz: " + balance + "\n")
    islem = input("Lütfen yapmak istediğiniz işlemi yazınız\n")
    islem = islem.lower()
    if 'cek' in islem or 'çek' in islem:
        paracekme(tcno)
    elif 'yatir' in islem or 'yatır' in islem:
        parayatirma(tcno)
    elif 'gonder' in islem or 'gönder' in islem or 'havale' in islem or 'eft' in islem or 'transfer' in islem:
        paragonderme(tcno)
    elif 'fatura' in islem or 'öde' in islem or 'ode' in islem:
        if int(balance)>0:
            fatura(tcno)
        else:
            print("Bu işlem için yeterli bakiyeniz bulunmamakta.\n")
            islemsecici(tcno)
    elif 'hesap' in islem or 'değiş' in islem or 'degis' in islem or 'başka' in islem or 'baska' in islem:
        print("Hesabınızdan çıkış yapılıyor.\nYeni hesap için ")
        login()
    elif 'çık' in islem or 'cik' in islem or 'çıkış' in islem or 'cikis' in islem or 'kapat' in islem or 'iptal' in islem:
        quit()
    else:
        print("İstediğiniz islem anlasilamadi. Şunları deneyebilirsiniz:\npara çekme\npara yatırma \npara gönderme\nfatura öde\nhesap değiştir\nçıkış \n")
        islemsecici(tcno)

 
def testint(tested_input):
    try:
        return int(tested_input)
    except ValueError:
        print("Lütfen sadece sayı giriniz.\n")
        login()
 
        
def login():
    taken_pass="null"
    taken_tcno = input("Lütfen 11 haneli tc numaranızı giriniz\n")
    testint(taken_tcno)
    if len(taken_tcno)!=11 or int(taken_tcno) <0:
        print("Tc numaranızı hatalı girdiniz. Tekrar deneyiniz.\n")
        login()        
    else:
        taken_pass= input("Lütfen şifrenizi giriniz\n")
        testint(taken_pass)
        control = db.search((User.tcno == taken_tcno) & (User.password == taken_pass ))   
        if control ==[]:  
            print("Hatalı Giriş\n")
            login()
        else:
            control = db.get(User.tcno == taken_tcno)
            isim = control.get('isim')
            tcno = control.get('tcno')            
            print("Giriş Başarılı!\n")
            print("Merhaba, "+ isim + " hoşgeldiniz.\n")           
            islemsecici(tcno)
            
    
    
db = TinyDB('db.json',ensure_ascii=False, encoding='utf-8')
User = Query()

login()
