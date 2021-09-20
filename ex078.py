'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
print(lista)
maior = menor = 0
lista2 = [0, 0]
for pos, v in enumerate(lista):
    print(pos, v)
    lista2.append(int(pos, v))
    print(lista2)
print('lista 2')
print(lista2)
print('max e min')
print(max(lista2))
print(min(lista2))
