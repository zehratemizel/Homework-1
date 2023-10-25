maas=float(input("Maaşı giriniz: "))
zamOrani=float(input("zam oranını giriniz: "))

#zam oranını ondalık sayıya dönüştürme
zam=zamOrani/100

#Artan maaşı hesaplama
artanMaas = maas * (1 + zam)
print("Çalışanın artan maaşı: ", artanMaas)