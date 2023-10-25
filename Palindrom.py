#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi=int(input("Bir sayı giriniz: "))

#Tersten okumak için [::-1] kullanılır.
palindrommu=str(sayi) == str(sayi)[::-1]

if palindrommu:
    print(f"{sayi} bir palindromik sayıdır.")
else:
    print(f"{sayi} bir palindromik sayı değildir.")