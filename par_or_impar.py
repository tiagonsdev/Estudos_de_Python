num = input('digite um numero inteiro: ')

try:

    numint = int(num)
    
    par_or_impar = numint % 2

    if(par_or_impar == 0):

        print('o numero é par')
    else:
        print('o numero é impar')

except:
    print('digite um numero valido')