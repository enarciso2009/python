'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
valores = list()
valoresimp = list()
valorespar = list()
while True:
    n = int(input("digite o valor: "))
    valores.append(n)
    resp = str(input('deseja continuar? [s/n]')).strip().upper()[0]
    if resp in 'Nn':
        break
    if n % 2 == 0:
        valorespar.append(n)
    else:
        valoresimp.append(n)
print('=-' * 30)
print(f'os numeros digitados foram {valores}')
print('=-' * 30)
print(f'os numeros digitados pares {valorespar}')
print('=-' * 30)
print(f'os numeros digitados impares {valoresimp}')
print('=-' * 30)
