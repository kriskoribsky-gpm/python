

text1=("Sedi mucha na stene, na stene, na stene."
       "Sedi mucha na stene, sedi a spi."
       "Sedi a buvinka potvorka malinka."
       "Sedi mucha na stene, sedi a spi.")

novytext1=(" ")
print("Nahradím  v texte <sedi mucha na stene> všetky samohlásky.")
    
pismeno=input("Akým písmenom chceš zameniť všetky samohlásky?")

for i in range(0,len(text1)):
    if  text1[i]=="a" or text1[i]=="e" or text1[i]=="i" or text1[i]=="o" or text1[i]=="u" or text1[i]=="ä" or text1[i]=="á" or text1[i]=="é" or text1[i]=="í" or text1[i]=="ó" or text1[i]=="ú":
        novytext1=novytext1+pismeno
    else:
        novytext1=novytext1+text1[i]
print (novytext1)
        


