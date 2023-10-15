pocet=int(input("Zadaj počet mien"))
prve=input("Zadaj 1. meno")

#str() = string -) vytvor z toho text

while meno != "":           #!= znamena, ze sa nerovna #while znamena ked
          meno=input("Zadaj "+str(i)+". meno")
          x=x+1      
          if prve > meno:
              prve=meno
print(prve)
