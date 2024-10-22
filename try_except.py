try:
    numero_str = input('vou dobrar o numero que voce digitar: ')

    numero_float = float(numero_str)

    print(f'o dobro do numero: {numero_float} é {numero_float * 2} ')
except:

    print(numero_str.isdigit())

    print('isso não é um numero')

    