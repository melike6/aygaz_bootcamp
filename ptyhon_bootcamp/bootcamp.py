import random


def tas_kagit_makas_MELİKE_SENA_ASLAN():
    print("Taş, Kağıt, Makas Oyunu Kuralları:")
    print("1. Taş, makası yener.")
    print("2. Kağıt, taşı yener.")
    print("3. Makas, kağıdı yener.")
    print("4. Aynı seçim yapılırsa oyun berabere biter.")
    print(
        "5. Her el sonunda, oyuna devam etmek isteyip istemediğiniz sorulacaktır. Eğer 'hayir' derseniz oyun sona erecektir."
    )
    print("6. İki turu kazanan oyunu kazanır.")


tas_kagit_makas_MELİKE_SENA_ASLAN()

secenekler = [
    "tas",
    "kagit",
    "makas",
]
k = 0
b = 0

while True:

    kullanici = input(
        "tas, kagit veya makas seçin, oyundan cikmak icin hayir yazin : "
    ).lower()

    if kullanici == "hayir":
        print()
        print("Başka bir oyun oynamak ister misiniz?")
        break
    elif kullanici not in secenekler:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        continue

    bilgisayar = random.choice(secenekler)
    print(f"Bilgisayarın seçimi: {bilgisayar}")

    if kullanici == bilgisayar:
        print("Berabere!")
    elif (
        kullanici == "tas"
        and bilgisayar == "makas"
        or kullanici == "makas"
        and bilgisayar == "kagit"
        or kullanici == "kagit"
        and bilgisayar == "tas"
    ):
        print("Kazandiniz!")
        k += 1
        if k == 2:
            print("Tebrikler oyunu kazandiniz!")
            break
    else:
        print("Kaybettiniz!")
        b += 1
        if b == 2:
            print("Oyunu kaybettiniz.")
            break
