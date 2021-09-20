'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
'''

popa = int(input("População A: "))
popb = int(input("População B: "))
cont = 0
while popa < popb:
    popa = (popa + (popa*3/100))
    popb = (popb + (popb*1/100))
    cont += 1
print('As Populações A {:.2f} e B {:.2f} se aproximariam em {} anos'.format(popa, popb, cont))
