
# Estou criando um videogame de fantasia.

#1º vamos usar um dicionario para descrever o item na "mochila"/dicionario,
# ou seja o valor_chave vai ser um item, e o valor dessa chave será a quantidade
# de itens nela. Exemplo: 'ouro': 42, 'poção_vida': 5

#2º Escreva uma função chamada displayInventory()
# que pegaria qualquer “inventário” possível e o exibiria da seguinte forma:
'''
Inventário:
12 flechas
42 moedas de ouro
1 corda
6 tochas
1 adaga
Número total de itens: 62

'''

mochila_de_itens = {'adaga': 2,'poc_mana': 5,'poc_vida': 10, 'gold': 150}

mochila_de_itens2 = {'adaga': 2,'poc_mana': 5,'poc_vida': 10, 'gold': 5000}




def contador_itens(mochila):
    print("****Os items na mochila são****** ")
    
    total_itens1 = 0
    
    for i,q in mochila.items():
        print("item:" , i) 
        print("Quantidade:" , q)
        total_itens1 = total_itens1 + q
        print()
    print(" A quantidade total de itens é: " , total_itens1)

contador_itens(mochila_de_itens)