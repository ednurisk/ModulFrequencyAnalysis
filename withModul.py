import myModul

text=input("please input your text: ")
#uzunluk= len(text) 
uzunluk=myModul.myLen(text)

#text=text.lower()
text=myModul.myLower(text)
print(uzunluk)

charactersCount={}
for characters in text:
    if characters in charactersCount:
        charactersCount[characters]+=1
    else:
        charactersCount[characters]=1

#sirali_harfler = sorted(charactersCount.items())
sirali_harfler=myModul.mySorted(charactersCount)


'''for characters, sayi in sirali_harfler:
 print(f"'{characters}': {sayi} adet, using rate:{sayi/uzunluk*100}") '''
myModul.myUsingRate(sirali_harfler.items(), uzunluk)

myModul.myMe()