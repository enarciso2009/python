'''
PROGRAMA PRINCIPAL
'''






'''
CRIAÇÃO DOS JOGADORES
'''
banco_f = 0
c = 0
n = int(input('Quantidade de jogadores: '))
dic = {'nome':'nome','valor': 0}
lista = list()
while c < n:
    for x in range(1, n + 1):
        nome = str(input(f'Nome {x} jogador: ')).upper()
        valor = int(5000)
        c += 1
        lista.append([nome, valor])
        participantes = dict(lista)

participantes['BANCO'] = 50000

print('-' * 30)

print(participantes)

print('-' * 30)

while True:
    while True:
        nome_r = str(input('Entre com o nome do remetente: [FIM para Sair] ')).upper()
        if nome_r in participantes or nome_r == 'FIM':
            break
        else:
            print('ERRO! digite um participante valido:')
    if nome_r == 'FIM':
        break
    while True:
        n  = str(input('Entre com o valor do pix: '))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Erro! digite um valor inteiro sem pontos ou virgulas.')
    while True:
        nome_d = str(input('Entre com o nome do destinatario: ')).upper()
        if nome_d in participantes:
            break
        else:
            print("ERRO! digite um participante valido:")
    participantes[nome_d] += valor
    participantes[nome_r] -= valor
    print()
    print('TABELA ATUALIZADA'.center(36))
    print('-' * 40)
    print('{:<28}'.format('NOME'),'{:>8}'.format('SALDO'))
    print()
    for k, v in participantes.items():
        print(f'{k:<28} {v:>8}')

    print('-' * 40)

print('-' * 30)

print()
print('TABELA ATUALIZADA'.center(36))
print('-' * 40)
print('{:<28}'.format('NOME'),'{:>8}'.format('SALDO'))
print()
for k, v in participantes.items():
    print(f'{k:<28} {v:>8}')


print('-' * 30)
