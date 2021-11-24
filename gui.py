'''
PROGRAMA GUI
'''

import tkinter
from tkinter import *
from jogo import exibe_lista





class MinhaGui:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.geometry('300x200')
        self.janela_principal.title('BANCO IMOBILIARIO')

        self.frame_cabecalho = Frame(self.janela_principal)
        self.frame_participante1 = Frame(self.janela_principal)
        self.frame_participante2 = Frame(self.janela_principal)
        self.frame_participante3 = Frame(self.janela_principal)
        self.frame_participante4 = Frame(self.janela_principal)
        self.frame_participante5 = Frame(self.janela_principal)
        self.frame_participante6 = Frame(self.janela_principal)
        self.frame_participante7 = Frame(self.janela_principal)

        self.label = Label(self.frame_cabecalho, text = 'Cadastro dos participantes:')
        self.label.pack(side='left')

        self.part1 = Label(self.frame_participante1, text = 'participante 1: ')
        self.part1.pack(side='left')
        self.part2 = Label(self.frame_participante2, text = 'participante 2: ')
        self.part2.pack(side='left')
        self.part3 = Label(self.frame_participante3, text = 'participante 3: ')
        self.part3.pack(side='left')
        self.part4 = Label(self.frame_participante4, text = 'participante 4: ')
        self.part4.pack(side='left')
        self.part5 = Label(self.frame_participante5, text = 'participante 5: ')
        self.part5.pack(side='left')
        self.part6 = Label(self.frame_participante6, text = 'participante 6: ')
        self.part6.pack(side='left')

        self.entrada_1 = Entry(self.frame_participante1, width = 20)
        self.entrada_1.bind('')
        self.entrada_1.pack(side='left')
        self.entrada_2 = Entry(self.frame_participante2, width = 20)
        self.entrada_2.bind('')
        self.entrada_2.pack(side='left')
        self.entrada_3 = Entry(self.frame_participante3, width = 20)
        self.entrada_3.bind('')
        self.entrada_3.pack(side='left')
        self.entrada_4 = Entry(self.frame_participante4, width = 20)
        self.entrada_4.bind('')
        self.entrada_4.pack(side='left')
        self.entrada_5 = Entry(self.frame_participante5, width = 20)
        self.entrada_5.bind('')
        self.entrada_5.pack(side='left')
        self.entrada_6 = Entry(self.frame_participante6, width = 20)
        self.entrada_6.bind('')
        self.entrada_6.pack(side='left')

        self.botao = Button(self.frame_participante7, text = 'Incluir Parcipantes', command = self.exibe)
        self.botao.pack(side='left')

        self.frame_cabecalho.pack()
        self.frame_participante1.pack()
        self.frame_participante2.pack()
        self.frame_participante3.pack()
        self.frame_participante4.pack()
        self.frame_participante5.pack()
        self.frame_participante6.pack()
        self.frame_participante7.pack()
        self.janela_principal.mainloop()

    def exibe(self):

        self.recebe(self.entrada_1.get())
        #print(self.entrada_2.get())
        #print(self.entrada_3.get())
        #print(self.entrada_4.get())
        #print(self.entrada_5.get())
        #print(self.entrada_6.get())

    def recebe(self, nom):
        lista = list()
        self.valor = 5000
        if not self.entrada_1.get():
            print('vazio')
        else:
            self.nome = self.entrada_1.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)

        if not self.entrada_2.get():
            print('vazio')
        else:
            self.nome = self.entrada_2.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)

        if not self.entrada_3.get():
            print('vazio')
        else:
            self.nome = self.entrada_3.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)

        if not self.entrada_4.get():
            print('vazio')
        else:
            self.nome = self.entrada_4.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)

        if not self.entrada_5.get():
            print('vazio')
        else:
            self.nome = self.entrada_5.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)

        if not self.entrada_6.get():
            print('vazio')
        else:
            self.nome = self.entrada_6.get().upper()
            lista.append(self.nome)
            lista.append(self.valor)
        # BANCO
        lista.append('BANCO')
        lista.append(50000)

        print(f'lista da MinhaGui {lista}')
        exibe_lista(lista)
        #MeuCadastro.cadastro(event.widget.get())

gui = MinhaGui()
