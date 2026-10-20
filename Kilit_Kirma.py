# Kırmızı renk için ANSI kodu
print("\033[31mBu yazı kırmızı renktedir!\033[0m")

# Yeşil renk için ANSI kodu
print("\033[32mBu yazı yeşil renktedir!\033[0m")

# Sarı renk için ANSI kodu
print("\033[33mBu yazı sarı renktedir!\033[0m")

# Normal yazı (renksiz)
print("Bu yazı normal renktedir.")

print("---------Kilit Kırma Oyununa Hoşgeldiniz---------")
print("Sistem gizli 3 haneli bir kombinasyon belirledi.")
print("Her basamak 0 ile 9 arasında farklı rakamlardan oluşur.")
print("Kombinasyonu bulmak için 3 hakkın var!\n")
gizli_sifre=[2,1,0]
hak=3
oyunu_kazandimi=False
while hak > 0:
    try:
        basamak1=int(input("1. basamağı giriniz: "))
        basamak2=int(input("2. basamağı giriniz: "))  
        basamak3=int(input("3. basamağı giriniz: "))
        tahmin=[basamak1,basamak2,basamak3]
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        continue
    if tahmin==gizli_sifre:
        print("\033[32mTebrikler! Kombinasyonu doğru tahmin ettiniz.\033[0m")
        oyunu_kazandimi=True
        break
    print("İp uçları: ")
    if tahmin[0]==gizli_sifre[0]:
        print("\033[32m1. basamak doğru.\033[0m")
    elif tahmin[0] in gizli_sifre:
        print("\033[33m1. basamak yanlış ama kombinasyonda var.\033[0m")
    else:
        print("\033[31m1. basamak yanlış ve kombinasyonda yok.\033[0m")
    if tahmin[1]==gizli_sifre[1]:
        print("\033[32m2. basamak doğru.\033[0m")
    elif tahmin[1] in gizli_sifre:
        print("\033[33m2. basamak yanlış ama kombinasyonda var.\033[0m")
    else:
        print("\033[31m2. basamak yanlış ve kombinasyonda yok.\033[0m")
    if tahmin[2]==gizli_sifre[2]:
        print("\033[32m3. basamak doğru.\033[0m")
    elif tahmin[2] in gizli_sifre:
        print("\033[33m3. basamak yanlış ama kombinasyonda var.\033[0m")
    else:  
        print("\033[31m3. basamak yanlış ve kombinasyonda yok.\033[0m")
    hak -= 1
    print(f"Kalan hakkınız: {hak}\n")
if not oyunu_kazandimi:
    print("\033[31mÜzgünüm, hakkınız bitti. Kombinasyon: ", gizli_sifre,"\033[0m")
        