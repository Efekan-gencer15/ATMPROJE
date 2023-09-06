print("""
      ********************************
            
      
      
       SİSTEME HOŞGELİDİNİZ !!!




      
      ********************************""")


print( """
      
      İşlemler:
      
      1.Bakiye Sorgulama
      
      2.Para Yatırma
      
      3.Para Çekme """ )

bakiye = 1000

while True:
    işlem = input("İşlem Giriniz:")

    if (işlem == "q" ):
        print("Yine Bekleriz : ")
        break

    elif (işlem =="1"):
        print ("Bakiyeniz {} TLdir".format(bakiye))
        
    elif (işlem == "2" ):
        miktar = int(input("Yatırmak İstediğiniz Tutar :"))
                     
        bakiye += miktar
    elif (işlem == "3" ):
        miktar = int(input("Çekmek İstediğiniz Tutar :"))
        if (bakiye - miktar < 0):
            print ("Yetersiz Bakiye")
            print ("Bakiyeniz : {} TL'dir".format(bakiye)) 
            continue
        bakiye -= miktar    
    else:
        print ("Lütfen Geçerli Bir İşlem Giriniz ...")