'''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

n = total = cont =0
while n != 999:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    total += n
    cont += 1
print('fim')
print(f"o total dos numeros digitados {total} e a quantidade de numeros digitados {cont}")
