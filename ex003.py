
'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''


print('digite as suas informações: ')
nome = str(input("Digite o seu nome: "))
idade = int(input("digite a sua idade: "))
salario = float(input("digite o seu salario: "))
sexo = str(input("digite o sexo [F/M]: ")).upper()
civil = str(input("digite o Estado Civil[S, C, V, D] ")).upper()
while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("A coisa ta difícil, mas não tem salário negativo: "))

while (sexo!= 'F') and (sexo!='M'):
    sexo = input("Biologicamente, você deve ser 'F' ou 'M': ").upper()

while (civil != 'S')and(civil != 'C')and(civil != 'V')and(civil != 'D'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser S, C, V ou D: ").upper()

print(f"dados, {nome}, {idade}, {salario}, {sexo}, {civil}")
