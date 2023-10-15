

text1=("Sedi mucha na stene, na stene, na stene.")
text2=("Sedi mucha na stene, sedi a spi.")
text3=("Sedi a buvinka potvorka malinka.")
text4=("Sedi mucha na stene, sedi a spi.")

novytext1=(" ")
novytext2=(" ")
novytext3=(" ")
novytext4=(" ")

print("Nahradím  v texte <sedi mucha na stene> všetky samohlásky.")
zobrazit=input("Chceš zobraziť text pesničky ? (ano/nie)")
if zobrazit == "ano":
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    
pismeno=input("Akým písmenom chceš zameniť všetky samohlásky?")

for i in range(0,len(text4)):
    if  text4[i]=="a" or "e" or "i" or "o" or "u" or "ä" or "á" or "é" or "í" or "ó" or "ú":
        print("dopiče")


