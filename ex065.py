
totalmais = totalmenos = cont = menor = maior = n = int(0)
while n != 999:
    n = int(input('digite um numero: '))
    if n != 999 and n > menor:
        totalmais =+ n
        maior = n
        cont += 1
        print("entrou no if")
    elif n != 999 and maior < n:
        totalmenos += n
        menor = n
        print('entrou no elif')
total = totalmais + totalmenos
print('menor {}, maior {} e a quantidade de numeros que digitou {} e valor total {}'.format(menor, maior, cont, total))


"""
n = total = cont = menor = maior = 0

while n != 999:
    n = int(input("Digite um numero: [999 para sair]  "))
    if n != 999:
        total += n
        cont += 1
        if menor < n :

        print("total {}".format(total))
    else:

        print("Fechando o sistema")
print("FIM Você digitou {} vezes e o total foi de {}".format(cont, total))
"""
