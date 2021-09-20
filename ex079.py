'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valor = []
while True:
    n = int(input("Digite um valor: "))
    valor.append(n)
    if valor.count(n) > 1:
        print('este valor ja foi digitado e será apagado:')
        valor.remove(n)
    resp = str(input('deseja continuar? '))
    if resp != 's':
        break
    #if valor.index(n) :
#        print('Este numero já foi digitado!')
print(valor)
valor.sort()
print(f'os numeros digitados em ordem foram = {valor}')
