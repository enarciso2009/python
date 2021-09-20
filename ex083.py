'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

lista = list()
lista.append(str(input('digite uma expresão Numerica: ')))
print(f'a expressão digitada foi = {lista}')
if lista.count(() == lista.count()):
    print('A expressão esta correta!!!')
else:
    print('a sua Expressão esta errada ficou faltando parenteses...')
