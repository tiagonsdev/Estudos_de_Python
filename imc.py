nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = int(input("Digite o seu peso: "))
imc = peso/altura ** 2

texto = f"seu nome é:  {nome}  sua altura é:  {altura:.2f}  seu peso:  {peso}"
imc = f"e seu imc é:  {imc:.2f}"

print(texto, imc)

