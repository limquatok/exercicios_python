
# Imagine que o saque de um dragão derrotado seja representado como uma lista de sequências como esta:
# dragonLoot = ['moeda de ouro', 'adaga', 'moeda de ouro', 'moeda de ouro', 'rubi']

# eu tenho que criar um função para adicionar os valores de uma lista(items do dragao morto) ao dicinario(mochila)

# essa função tem que ter 2 parametros o dicinario e a lista: adicionarItems(lista,dicinario):

# a função tem que retorna os valores do dicionario(mochila) atualizados

mochila_de_itens = {'adaga': 2,'poc_mana': 5,'poc_vida': 10, 'gold': 150}

mochila_de_itens2 = {'adaga': 2,'poc_mana': 5,'poc_vida': 10, 'gold': 5000}

recompensa_dragao_morto = ['gold', 'adaga', 'gold', 'gold', 'rubi','espada de fogo']





def espolio_do_dragao(mochila,espolio):
    
    total_items = 0
    
    print("Seus itens antes do dragao morto: ")
    for chave,item in mochila.items():        
        print(chave , item)
    print()
    
    print("***************************")
    print("*Recompeça do dragao:     *")
    
    for i in espolio:
       
        print("*",       i ,            )
    
    print("***************************")
    print()
    
    for item in espolio:
        
        if item in mochila_de_itens:
            
            mochila[item] =  mochila[item] + 1
            #print(mochila)

        if item not in mochila:
            
            mochila.setdefault(item, 1)
            #print(mochila)
            
     
    print("Quantidade de itens obtidos do dragao: " , len(espolio))
    print()
    
        
    print("Seus itens agora: ")
    for chave,item in mochila.items():        
        total_items = total_items + item
        print(chave , item)

    print("valor total de items na mochila: ", total_items)
    print()
    
espolio_do_dragao(mochila_de_itens,recompensa_dragao_morto)