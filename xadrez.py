tabuleiro = {
'a1': 'w-torre','b1': 'w-cavalo','c1': 'w-bispo',
'd1': 'w-rainha','e1': 'w-rei','f1': 'w-bispo',
'g1': 'w-cavalo','h1': 'w-torre',

'a2': 'w-peao','b2': 'w-peao','c2': 'w-peao',
'd2': 'w-peao','e2': 'w-peao','f2': 'w-peao',
'g2': 'w-peao','h2': 'w-peao',

'a3': ' ','b3': ' ','c3': ' ',
'd3': ' ','e3': ' ','f3': ' ',
'g3': ' ','h3': ' ',

'a4': ' ','b4': ' ','c4': ' ',
'd4': ' ','e4': ' ','f4': ' ',
'g4': ' ','h4': ' ',

'a5': ' ','b5': ' ','c5': ' ',
'd5': ' ','e5': ' ','f5': ' ',
'g5': ' ','h5': ' ',

'a6': ' ','b6': ' ','c6': ' ',
'd6': ' ','e6': ' ','f6': ' ',
'g6': ' ','h6': ' ',

'a7': 'b-peao','b7': 'b-peao','c7': 'b-peao',
'd7': 'b-peao','e7': 'b-peao','f7': 'b-peao',
'g7': 'b-peao','h7': 'b-peao',

'a8': 'b-torre','b8': 'b-cavalo','c8': 'b-bispo',
'd8': 'b-rainha','e8': 'b-rei','f8': 'b-bispo',
'g8': 'b-cavalo','h8': 'b-torre',
}



print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a1'],"|", "|", tabuleiro['b1'],"|", "|", tabuleiro['c1'],"|","|",tabuleiro['d1'],"|","|",tabuleiro['e1'],"|","|",tabuleiro['f1'],"|","|",tabuleiro['g1'],"|","|",tabuleiro['h1'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

print(" ________","  _________"," _________"," _________"," _________"," _________"," _________"," _________")
print("|",tabuleiro['a2'],"|", "|", tabuleiro['b2'],"|", "|", tabuleiro['c2'],"|","|",tabuleiro['d2'],"|","|",tabuleiro['e2'],"|","|",tabuleiro['f2'],"|","|",tabuleiro['g2'],"|","|",tabuleiro['h2'],"|")
print("|________|" , "|________|", "|________|", "|________|", "|________|" , "|________|" , "|________|" , "|________|")

print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a3'],"|", "|", tabuleiro['b3'],"|", "|", tabuleiro['c3'],"|","|",tabuleiro['d3'],"|","|",tabuleiro['e3'],"|","|",tabuleiro['f3'],"|","|",tabuleiro['g3'],"|","|",tabuleiro['h3'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a4'],"|", "|", tabuleiro['b4'],"|", "|", tabuleiro['c4'],"|","|",tabuleiro['d4'],"|","|",tabuleiro['e4'],"|","|",tabuleiro['f4'],"|","|",tabuleiro['g4'],"|","|",tabuleiro['h4'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a5'],"|", "|", tabuleiro['b5'],"|", "|", tabuleiro['c5'],"|","|",tabuleiro['d5'],"|","|",tabuleiro['e5'],"|","|",tabuleiro['f5'],"|","|",tabuleiro['g5'],"|","|",tabuleiro['h5'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a6'],"|", "|", tabuleiro['b6'],"|", "|", tabuleiro['c6'],"|","|",tabuleiro['d6'],"|","|",tabuleiro['e6'],"|","|",tabuleiro['f6'],"|","|",tabuleiro['g6'],"|","|",tabuleiro['h6'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

print(" ________","  _________"," _________"," _________"," _________"," _________"," _________"," _________")
print("|",tabuleiro['a7'],"|", "|", tabuleiro['b7'],"|", "|", tabuleiro['c7'],"|","|",tabuleiro['d7'],"|","|",tabuleiro['e7'],"|","|",tabuleiro['f7'],"|","|",tabuleiro['g7'],"|","|",tabuleiro['h7'],"|")
print("|________|" , "|________|", "|________|", "|________|", "|________|" , "|________|" , "|________|" , "|________|")


print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
print("|",tabuleiro['a8'],"|", "|", tabuleiro['b8'],"|", "|", tabuleiro['c8'],"|","|",tabuleiro['d8'],"|","|",tabuleiro['e8'],"|","|",tabuleiro['f8'],"|","|",tabuleiro['g8'],"|","|",tabuleiro['h1'],"|")
print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")


def funcao_print_tabuleiro():
    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a1'],"|", "|", tabuleiro['b1'],"|", "|", tabuleiro['c1'],"|","|",tabuleiro['d1'],"|","|",tabuleiro['e1'],"|","|",tabuleiro['f1'],"|","|",tabuleiro['g1'],"|","|",tabuleiro['h1'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")


    print(" ________","  _________"," _________"," _________"," _________"," _________"," _________"," _________")
    print("|",tabuleiro['a2'],"|", "|", tabuleiro['b2'],"|", "|", tabuleiro['c2'],"|","|",tabuleiro['d2'],"|","|",tabuleiro['e2'],"|","|",tabuleiro['f2'],"|","|",tabuleiro['g2'],"|","|",tabuleiro['h2'],"|")
    print("|________|" , "|________|", "|________|", "|________|", "|________|" , "|________|" , "|________|" , "|________|")

    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a3'],"|", "|", tabuleiro['b3'],"|", "|", tabuleiro['c3'],"|","|",tabuleiro['d3'],"|","|",tabuleiro['e3'],"|","|",tabuleiro['f3'],"|","|",tabuleiro['g3'],"|","|",tabuleiro['h3'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a4'],"|", "|", tabuleiro['b4'],"|", "|", tabuleiro['c4'],"|","|",tabuleiro['d4'],"|","|",tabuleiro['e4'],"|","|",tabuleiro['f4'],"|","|",tabuleiro['g4'],"|","|",tabuleiro['h4'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a5'],"|", "|", tabuleiro['b5'],"|", "|", tabuleiro['c5'],"|","|",tabuleiro['d5'],"|","|",tabuleiro['e5'],"|","|",tabuleiro['f5'],"|","|",tabuleiro['g5'],"|","|",tabuleiro['h5'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a6'],"|", "|", tabuleiro['b6'],"|", "|", tabuleiro['c6'],"|","|",tabuleiro['d6'],"|","|",tabuleiro['e6'],"|","|",tabuleiro['f6'],"|","|",tabuleiro['g6'],"|","|",tabuleiro['h6'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")

    print(" ________","  _________"," _________"," _________"," _________"," _________"," _________"," _________")
    print("|",tabuleiro['a7'],"|", "|", tabuleiro['b7'],"|", "|", tabuleiro['c7'],"|","|",tabuleiro['d7'],"|","|",tabuleiro['e7'],"|","|",tabuleiro['f7'],"|","|",tabuleiro['g7'],"|","|",tabuleiro['h7'],"|")
    print("|________|" , "|________|", "|________|", "|________|", "|________|" , "|________|" , "|________|" , "|________|")


    print(" _________","  __________"," __________"," ___________"," ________"," __________","  __________","  _________")
    print("|",tabuleiro['a8'],"|", "|", tabuleiro['b8'],"|", "|", tabuleiro['c8'],"|","|",tabuleiro['d8'],"|","|",tabuleiro['e8'],"|","|",tabuleiro['f8'],"|","|",tabuleiro['g8'],"|","|",tabuleiro['h1'],"|")
    print("|_________|" , "|__________|", "|_________|", "|__________|", "|_______|" , "|_________|" , "|__________|" , "|_________|")





def verfica_Xadrez(local_peca):
    
        print("Digite qual peça voce quer mover")
        peca = input()
            
        print("Voce digitou o local: " , local_peca, " para a peça: " , peca)
            
        if local_peca in tabuleiro:
        
            tabuleiro[local_peca] = peca
            funcao_print_tabuleiro()  
            
            print(True)
          
        else:
            print(" O local que voce mecheu a peça não existe escolha uma casa dentro do tabuleiro!")        
            funcao_print_tabuleiro() 
           
            print(False)
          

verfica_Xadrez('asda')
