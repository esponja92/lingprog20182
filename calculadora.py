loop = 1

while(loop):

    numero_1 = input("Entre com o primeiro numero da conta: ")
    numero_2 = input("Entre com o segundo numero da conta: ")
    op = input("digite 1 para soma, 2 para subtracao, 3 para multiplicacao ou 4 para divisao: ")
    resultado = 0

    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
    op = float(op)

    if op == 1:
        resultado = numero_1 + numero_2
    if op == 2:
        resultado = numero_1 - numero_2
    if op == 3:
        resultado = numero_1 * numero_2
    if op == 4:
        resultado = numero_1 / numero_2

    print("O resultado da operacao e igual a: ",resultado)
    loop = input("Digite 1 para continuar calculado ou 0 para encerrar o programa: ")
    loop = int(loop)


