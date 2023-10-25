#Vücut kütke indeksi hesaplama
boy=float(input("Lütfen boyunuzu giriniz: "))

agirlik=float(input("Lütfen ağırlığınızı giriniz: "))

vki=(agirlik/(boy**2))

if vki < 18 :
    print(("Vücut kitle indexiniz zayıf"), "vki:" , vki)

elif vki<25:
    print(("Vücut kitle indexiniz normal"),"vki:" , vki)

elif vki<30:
    print(("Vücut kitle indexiniz kilolu"), "vki:" , vki)

else:
    print(("Vücut kitle indexiniz obez"), "vki:" , vki)



