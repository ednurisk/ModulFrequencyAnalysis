text=input("please input your text: ")
uzunluk= len(text)
text=text.lower()
print(uzunluk)

charactersCount={}

for characters in text:
    if characters in charactersCount:
        charactersCount[characters]+=1
    else:
        charactersCount[characters]=1

sirali_harfler = sorted(charactersCount.items())

for characters, sayi in sirali_harfler:
 print(f"'{characters}': {sayi} adet, using rate:{sayi/uzunluk*100}")



