nome = input('escreva seu nome: ')

if(len(nome) <= 4):
    print('seu nome é curto :)')

elif(len(nome) >= 5 and len(nome) <= 6 ):
    print('seu nome é normal :)')

elif(len(nome) >= 7):
    print('seu nome é enorme :)')