import tkinter as tk


def populate(frame):
    global widgets
    widgets={}

    '''Put in some fake data'''
    tk.Label(frame, text='X',background='white').grid(row=0, column=0,padx=10,pady=5)
    tk.Label(frame, text='K',background='white').grid(row=0, column=1,padx=10,pady=5)
    tk.Label(frame, text='S',background='white').grid(row=0, column=2,padx=10,pady=5)
    tk.Label(frame, text='(%)',background='white').grid(row=0, column=3,padx=10,pady=5)

    for row in range(1,100):

        tk.Label(frame, text="%s" % row, width=3, borderwidth="1",
                 relief="solid").grid(row=row, column=0)
        t="this is the second column for row %s" %row
        tk.Label(frame, text=t).grid(row=row, column=1)
        tk.Label(frame, text='ANOTHER COLUMN'+str(row)).grid(row=row,column=2)


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

table_root = tk.Tk()
canvas = tk.Canvas(table_root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(table_root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

table_root.mainloop()
