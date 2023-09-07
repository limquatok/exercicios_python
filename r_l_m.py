# Esse é um exercicio do livro (Automate the Boring Stuff with Python) mais precisamente
# o exercicio do capitulo 4 de " lista em python ", deixarei o link do livro no arquivo readme.

import random
#lista para guarda a sequencia de 6 caracter T ou H
cara_coroa = []

#contadores
contador_cara = 0
contador_coroa = 0

#For aninhado:
#For para repetir dez mil vezes: 
for x in range(10000):
   
#for para repetir 6 vezes
    for y in range(6):
        
# if com a função randint, caso o numero aleatorio seja = 0 o if é executado.
        if random.randint(0,1) == 0:
# usando a função append() para adicinar ao final de cada item da minha lista o caracter H.
            cara_coroa.append('H')
# caso o numero aletorio seja 1 o else e executado.
        else:
# adiciona o caracter "T" na minha lista.
            cara_coroa.append('T')
               
# Função all retorna um bool com isso faço uma vericarção se os 6 primeiros caracter são iguais a "H" .       
    cara = all('H' == item for item in cara_coroa[0:6])
    
# Faço a mesma coisa aqui agora com coroa que no caso é representado pelo caracter "T".
    coroa= all('T' == item for item in cara_coroa[0:6])
   
#como minha função retorna um True ou False aqui eu verico se minha variavel é True, se sim, o if é
# executado.   
    if cara:
        ''' PARA NÂO POLUIR A TELA print("A minha lista tem de 1 a 6 caracter H")'''
#contador para guarda as vezes que que teve a sequencia de 6 "H"
        contador_cara += 1
       
# mesma coisa aqui caso a função all retorne um Treu o if executado
    if coroa:
        ''' PARA NÂO POLUIR A TELA ("A minha lista tem de 1 a 6 caracter T") '''
#contador para guarda as vezes que que teve a sequencia de 6 "H"
        contador_coroa += 1
    '''
    Para NÂO POLUIR A tela
    else:
        #print("Não tem sequencia de caracter!")
    '''
 # Quando meu 2 for adiciona os 6 caracter na minha lista eu limpo ela com a função clear,
 # para que eu conte novamente se teve uma sequencia de 6 caracter.
    cara_coroa.clear()

# calculo de percentual 
percentual_cara = (contador_cara / 100) 
percentual_coroa = (contador_coroa / 100)

print("porcentagem de vezes que caiu cara: " , str(float(percentual_cara)) + " %")
print("porcentagem de vezes que caiu coroa: " , str(float(percentual_coroa)) + " %")


