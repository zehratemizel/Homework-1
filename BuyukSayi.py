#Girilen sayılar arasında en büyüğünü bulma. (tamsayı)
x=int(input("1. sayıyı giriniz: "))
y=int(input("2. sayıyı giriniz: "))
z=int(input("3. sayıyı giriniz "))

if (x>y and x>z):
    buyuk=x

elif (y>x and y>z):
    buyuk=y
else:
    buyuk=z

print("Girilen en büyük sayı: " ,buyuk)
 
