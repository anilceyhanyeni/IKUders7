import random
cevap = "e"
while cevap == "e":
    alt = int(input("UST SINIR:"))
    ust = int(input("ALT SINIR:"))
    if alt > ust:
        alt, ust = ust, alt
              
    s = random.randint(alt,ust)
    tahmin = 0

    t = 0

    while t!=s:
        tahmin = tahmin + 1
        print(tahmin, '. tahmininiz ? ', end = ' ')
        t = int(input())
        if t<s:
            print("Benim sayim daha buyuk.")
        elif t>s:
            print("Benim sayim daha kucuk.")
        else:
            print("Tebrikler")
            print("Benim tuttugum sayi:",s,"idi")
            print(tahmin, "tahminde buludunuz")
            
    cevap = input("Tekrar oynamak ister misiniz (e/h) = ")

print("Güle Güle")
