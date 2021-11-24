from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from teste import *


def retrieve_input():
    input = self.myText_Box.get("1.0",END)


def cadastro(var):
    lista = list()
    if var == 0:
        lista.append(cadum = boxum.get('1.0', 'end -1c'))
        if len(cadum) > 0:
            ctum = 1
        else:
            ctum = 0
        caddois = boxdois.get('1.0', 'end -1c')
        if len(caddois) > 0:
            ctdois = 1
        else:
            ctdois = 0
        lista.append(cadtres = boxtres.get('1.0', 'end -1c'))
        if len(cadtres) > 0:
            cttres = 1
        else:
            cttres = 0
        lista.append(cadqua = boxqua.get('1.0', 'end -1c'))
        if len(cadqua) > 0:
            ctqua = 1
        else:
            ctqua = 0
        lista.append(cadcin = boxcin.get('1.0', 'end -1c'))
        if len(cadcin) > 0:
            ctcin = 1
        else:
            ctcin = 0
        lista.append(cadsei = boxsei.get('1.0', 'end -1c'))
        if len(cadsei) > 0:
            ctsei = 1
        else:
            ctsei = 0
        soma = ctum + ctdois + cttres + ctqua + ctcin + ctsei
        print(soma)
        participantes = dict(lista)
        print(participantes)

window = Tk()
window.title("Banco Imobiliario")
window.geometry('550x300')
tab_control = ttk.Notebook(window)
aba1 = ttk.Frame(tab_control)
aba2 = ttk.Frame(tab_control)
tab_control.add(aba1, text='Cadastro')
tab_control.add(aba2, text='Jogo')
lbl1 = Label(aba1, text= 'Participantes')
lbl1.grid(column=0, row=0)
lbl2 = Label(aba2, text= 'Pagar/Receber')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

#cod = Label(aba1, text = 'Codigo:')
#cod.grid(column=1, row=2)


partum = Label(aba1, text = 'Participante 1:')
partum.grid(column = 1, row = 1)
boxum=Text(aba1, height = 1, width = 30)
boxum.grid(column = 2, row = 1)

partdois = Label(aba1, text = 'Participante 2:')
partdois.grid(column = 1, row = 2)
boxdois = Text(aba1, height = 1, width = 30)
boxdois.grid(column = 2, row = 2)

parttres = Label(aba1, text = 'Participante 3:')
parttres.grid(column = 1, row = 3)
boxtres = Text(aba1, height = 1, width = 30)
boxtres.grid(column = 2, row = 3)

partqua = Label(aba1, text = 'Participante 4:')
partqua.grid(column = 1, row = 4)
boxqua =Text(aba1, height = 1, width = 30)
boxqua.grid(column = 2, row = 4)

partcin = Label(aba1, text = 'Participante 5:')
partcin.grid(column = 1, row = 5)
boxcin = Text(aba1, height = 1, width = 30)
boxcin.grid(column = 2, row = 5)

partsei = Label(aba1, text = 'Participante 6:')
partsei.grid(column=1, row=6)
boxsei = Text(aba1, height = 1, width = 30)
boxsei.grid(column = 2, row = 6)
var = 0
botaopart = Button(aba1, text = 'Incluir Participantes', command = tela_incluir())
botaopart.grid(column = 2, row = 7)

 # lambda:exibir_msg(var),

#botao = Button(aba1, text='Salvar', command = aba1.quit)
#botao.grid(column=2, row=6)




# aba Jogo

nomerm = Label(aba2, text = 'Nome Remetente:')
nomerm.grid(column = 2, row = 1)
textboxnr = Text(aba2, height = 1, width = 30)
textboxnr.grid(column = 3, row = 1)

valor = Label(aba2, text = 'Valor:')
valor.grid(column = 2, row = 3)
textboxv = Text(aba2,height = 1, width = 15)
textboxv.grid(column = 3, row = 3)

nomedes = Label(aba2, text = 'Nome Destinatario')
nomedes.grid(column = 2, row = 5)
textboxdes = Text(aba2, height = 1, width = 30)
textboxdes.grid(column = 3, row = 5)

botaoj = Button(aba2, text='Transferir', command = aba2.quit)
botaoj.grid(column = 3, row = 8)




#def hello_world(self):
#    messagebox.showinfo('Adoro a Apostila Python Progressivo!')
#    quit()



window.mainloop()
