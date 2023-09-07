import random
cara_coroa = []


contador_cara = 0
contador_coroa = 0

for x in range(10000):
   
    for y in range(6):
        
        if random.randint(0,1) == 0:
            cara_coroa.append('H')

        else:
            cara_coroa.append('T')
            
   
        
    cara = all('H' == item for item in cara_coroa[0:6])
    

    coroa= all('T' == item for item in cara_coroa[0:6])
   
    
    if cara:
        #print("A minha lista tem de 1 a 6 caracter H")
        contador_cara += 1
       

    if coroa:
        #print("A minha lista tem de 1 a 6 caracter T")
        contador_coroa += 1
    else:
        print("Não tem sequencia de caracter!")
        
    cara_coroa.clear()

percentual_cara = (contador_cara / 100) 
percentual_coroa = (contador_coroa / 100)

print("porcentagem de vezes que caiu cara: " , str(float(percentual_cara)) + " %")
print("porcentagem de vezes que caiu coroa: " , str(float(percentual_coroa)) + " %")


