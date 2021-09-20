'''Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
'''


n = int(input("Digite um numero de [0/10]: "))
print(n)
while n != -1:
    if n >= 0  and n<=10:
        print("parabens digitou o numero correto:")
        n = int(input('deseja entrar com um novo numero: ou [-1 para sair] '))
    else:
        print("digitos invalidos:")
        n = int(input("digite novamente: ou [-1 para sair] "))
print("Sistema Finalizado")
