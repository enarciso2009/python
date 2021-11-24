import tkinter
from tkinter import *
from gui import *
from tkinter import messagebox


class MeuJogo:
    def __init__(self):
        self.janela_jogo = Tk()
        self.janela_jogo.geometry('300x200')
        self.janela_jogo.title('Transferencias Bancarias')

        self.frame_label = Frame(self.janela_jogo)
        self.frame_remetente = Frame(self.janela_jogo)
        self.frame_valor = Frame(self.janela_jogo)
        self.frame_destinatario = Frame(self.janela_jogo)
        self.frame_botao_transf = Frame(self.janela_jogo)

        self.label = Label(self.frame_label, text = 'Transferencias Bancarias')
        self.label.pack(side='left')

        self.label_remetente = Label(self.frame_remetente, text = 'Remetente')
        self.label_remetente.pack(side='left')
        self.entrada_remetente = Entry(self.frame_remetente, width = 20)
        self.entrada_remetente.pack(side='left')

        self.label_valor = Label(self.frame_valor, text = 'Valor R$')
        self.label_valor.pack(side='left')
        self.entrada_valor = Entry(self.frame_valor, width = 20)
        self.entrada_valor.pack(side='left')

        self.label_destina = Label(self.frame_destinatario, text = 'Destinatario')
        self.label_destina.pack(side='left')
        self.entrada_destina = Entry(self.frame_destinatario, width = 20)
        self.entrada_destina.pack(side='left')

        self.botao_transacao = Button(self.frame_botao_transf, text = 'Transferencia',
        command = self.exibe_lista)
        self.botao_transacao.pack(side='left')

        self.frame_label.pack()
        self.frame_remetente.pack()
        self.frame_valor.pack()
        self.frame_destinatario.pack()
        self.frame_botao_transf.pack()


        mainloop()

    def exibe_lista(lista_p):
        lista_c = self.lista_p
        print(lista_c)


    def remetente(self):
        print(self.entrada_remetente.get())
        self.valor()


    def valor(self):
        print(self.entrada_valor.get())
        self.destinatario()


    def destinatario(self):
        print(self.entrada_destina.get())

'''
        while True:
            if self.entrada_remetente.get() in self.MinhaGui.self.lista:
                break
            else:
                messagebox.showinfo('Participante não encontrado' + self.entrada_remetente.get())
'''
'''
        nome_r = self.entrada_remetente.get()
        print(f'nome dentro do remetente {nome_r}')
        while True:
            while True:
                self.entrada_remetente = str(input('Entre com o nome do remetente: [FIM para Sair] ')).upper()
                if nome_r in self.MinhaGui.self.lista or nome_r == 'FIM':
                    break
                else:
                    print('ERRO! digite um participante valido:')
            if nome_r == 'FIM':
                break
'''




jogo = MeuJogo()
