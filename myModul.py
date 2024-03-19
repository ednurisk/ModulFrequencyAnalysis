def myLower(text):
    lower_text=""
    for character in text:
        if 'A' <= character <= 'Z':
            # Büyük harfi küçük harfe dönüştür
            lower_text += chr(ord(character) + 32)
        else:
            lower_text += character
    return lower_text



def myLen(text):
    uzunluk = 0
    for karakter in text:
        uzunluk += 1
    return uzunluk



def mySorted(dictionary):
    sirali_anahtarlar = list(dictionary.keys())
    n = len(sirali_anahtarlar)
    for i in range(n):
        for j in range(0, n-i-1):
            if sirali_anahtarlar[j] > sirali_anahtarlar[j+1]:
                sirali_anahtarlar[j], sirali_anahtarlar[j+1] = sirali_anahtarlar[j+1], sirali_anahtarlar[j]
    sirali_dictionary = {}
    for anahtar in sirali_anahtarlar:
        sirali_dictionary[anahtar] = dictionary[anahtar]
    return sirali_dictionary



def myUsingRate(sirali_harfler, uzunluk):
    for characters, sayi in sirali_harfler:
        rate = sayi / uzunluk * 100
        print(f"'{characters}': {sayi} adet, using rate:{rate:.2f}%")



def myMe():
    print("hello it's Eda Nur Isik and my school ID 211213049")