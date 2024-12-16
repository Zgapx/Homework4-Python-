# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def soru1(a):
    i=0
    b=input("Kelimeyi giriniz:")
    while(i<a):
        print(b)
        i+=1
soru1(7)     

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def soru2(a,b):
   print("Dikdörtgenin çevresi:"+str(2*(a+b)))
   print("Dikdörtgenin alanı:"+str(a*b))
soru2(2,5)

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
import random
def soru3():
    b=input("Yazı mı Tura mı?:")
    c=random.randint(1,2)
    if b=="Yazı" and c==1:
        print("Tebrikler! Yazı çıktı!")
    elif b=="Yazı" and c==2:
        print("Malesef Tura çıktı!")
    elif b=="Tura" and c==1:
        print("Malesef Yazı çıktı!")
    elif b=="Tura" and c==2:
        print("Tebrikler Tura çıktı!")
soru3()
    

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def soru4(a,b):
    asal=[]
    if(a<b):
        i=a+1
        while i<b:
            flag=1
            c=2
            while c<=i/2:
                if i%c==0:
                    flag=0
                    break
                c+=1
            if flag and i >1:
                asal.append(i)
            i+=1
    elif (a>b):
        i=b+1
        while i<a:
            flag=1
            c=2
            while c<=i/2:
                if i%c==0:
                    flag=0
                    break
                c+=1
            if flag and i >1:
                asal.append(i)
            i+=1
    return asal
print(soru4(32,13))



# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def soru5(a):
   bolen=[]
   i=1
   while(i<=a):
      if(a%i==0): 
        bolen.append(i)
      i+=1
   return bolen
print(soru5(762))

   