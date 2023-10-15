pocet=int(input("Zadaj počet mien"))
prve=input("Zadaj 1. meno")
#str() = string -) vytvor z toho text
for i in range(2,pocet+1):
          meno=input("Zadaj "+str(i)+". meno")
          if prve > meno:
              prve=meno
print(prve)
              
          
        
