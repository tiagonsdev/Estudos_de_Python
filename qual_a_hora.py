hora = input('digite a hora a hora:')

hora_float = float(hora)

if(hora_float >= 0 and hora_float <=5.59):

    print('Boa madruga')
elif(hora_float >=7 and hora_float<=11.59):

    print('Buenos Dias')

elif(hora_float >= 12 and hora_float <= 17.59):
    print('boas tardes')

elif(hora_float >=18 and hora_float <= 23.59):
    print('oyasuminasai')


