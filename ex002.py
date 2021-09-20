'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
'''
resp = 'S'

while resp in 'Ss':
    nome = str(input("digite o usuario: "))
    senha = str(input("digite a senha: "))

    if nome == senha:
        print("a senha precisa ser diferente do usuario")
        senha = str(input('digite a senha novamente: '))
    else:
        print('cadastro executado com sucesso:')
        resp = input("Deseja fazer um novo cadastro [S/N]").upper()
print("Fim do Cadastro")
