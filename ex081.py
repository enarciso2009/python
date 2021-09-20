'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    rest = str(input('deseja digitar outro valor? [s/n]')).strip().upper()[0]
    if rest in 'Nn':
        break
print('=-' * 30)
print(f'voce digitou {len(lista)} numeros')
print('=-' * 30)
# lista.sort(reverse=True)
lista.sort()
lista.reverse()
print(f'a lista sendo mostrada inversamente = {lista}')
print('=-' * 30)
if 5 in lista[:]:
    print('o numero 5 esta na lista')
else:
    print('o numero 5 não esta na lista')
print('=-' * 30)
