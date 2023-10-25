#Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.
import math
#yarıçapı kullanıcıdan al.
yaricap = float(input("Lütfen yarıçapı giriniz: "))

 #Çemberin alanını hesaplayın 
alan = math.pi * yaricap**2

#Çemberin çevresini hesaplayın
cevre = 2 * math.pi * yaricap

#Dairenin alanını ve çevresini yazdırın
print("Dairenin alanı: ", alan)
print("Dairenin çevresi: ", cevre)