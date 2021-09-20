'''
lista de preços com formatação feita com tuplas.
'''

lista = ('lapis', '1.99','caneta','2.29','caderno','15.00','borracha','0.59','mochila','120.00')

for n in range(0, len(lista)):
    if n % 2 == 0:
        print(lista[n])
    else:
        print(lista[n])
