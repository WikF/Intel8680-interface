from tkinter import *
from tkinter import ttk

def mov():
    first_registery = from_entry.get()[:2]
    secondregistery = from_entry.get()[2:]

    if secondregistery == 'AX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=2, sticky= E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'BX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=3, sticky= E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'CX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=4, sticky= E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'DX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=5, sticky= E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'AH':
        ttk.Label(mainframe, text=(dic[first_registery]+dic[secondregistery]), width=20).grid(column=2, row=2, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'BH':
        ttk.Label(mainframe, text=(dic[first_registery]+dic[secondregistery]), width=20).grid(column=2, row=3, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'CH':
        ttk.Label(mainframe, text=(dic[first_registery]+dic[secondregistery]), width=20).grid(column=2, row=4, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'DH':
        ttk.Label(mainframe, text=(dic[first_registery]+dic[secondregistery]), width=20).grid(column=2, row=5, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'AL':
        ttk.Label(mainframe, text=(dic[secondregistery]+dic[first_registery]), width=20).grid(column=2, row=2, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'BL':
        ttk.Label(mainframe, text=(dic[secondregistery]+dic[first_registery]), width=20).grid(column=2, row=3, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'CL':
        ttk.Label(mainframe, text=(dic[secondregistery]+dic[first_registery]), width=20).grid(column=2, row=4, sticky=E)
        dic[secondregistery] = dic[first_registery]

    if secondregistery == 'DL':
        ttk.Label(mainframe, text=(dic[secondregistery]+dic[first_registery]), width=20).grid(column=2, row=5, sticky=E)
        dic[secondregistery] = dic[first_registery]



def swap():
    first_registery = from_entry.get()[:2]
    secondregistery = from_entry.get()[2:]

    #AX:
    if first_registery == 'AX' and secondregistery == 'BX':
        ttk.Label(mainframe, text=dic[secondregistery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[first_registery], width=20).grid(column=2, row=3, sticky=E)
        dic['AX'], dic['BX'] = dic['BX'], dic['AX']

    if first_registery == 'BX' and secondregistery == 'AX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=3, sticky=E)
        dic['AX'], dic['BX'] = dic['BX'], dic['AX']


    if first_registery == 'AX' and secondregistery == 'CX':
        ttk.Label(mainframe, text=dic[secondregistery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[first_registery], width=20).grid(column=2, row=4, sticky=E)
        dic['AX'], dic['CX'] = dic['CX'], dic['AX']

    if first_registery == 'CX' and secondregistery == 'AX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=4, sticky=E)
        dic['AX'], dic['CX'] = dic['CX'], dic['AX']


    if first_registery == 'AX' and secondregistery == 'DX':
        ttk.Label(mainframe, text=dic[secondregistery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[first_registery], width=20).grid(column=2, row=5, sticky=E)
        dic['AX'], dic['DX'] = dic['DX'], dic['AX']

    if first_registery == 'DX' and secondregistery == 'AX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=2, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=5, sticky=E)
        dic['AX'], dic['DX'] = dic['DX'], dic['AX']

#BC
    if first_registery == 'BX' and secondregistery == 'CX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=4, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=3, sticky=E)
        dic['CX'], dic['BX'] = dic['BX'], dic['CX']

    if first_registery == 'CX' and secondregistery == 'BX':
        ttk.Label(mainframe, text=dic[first_registery], width=20).grid(column=2, row=3, sticky=E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=4, sticky=E)
        dic['CX'], dic['BX'] = dic['BX'], dic['CX']


    if first_registery == 'BX' and secondregistery == 'DX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=5, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=3, sticky=E)
        dic['DX'], dic['BX'] = dic['BX'], dic['DX']


    if first_registery == 'DX' and secondregistery == 'BX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=3, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=5, sticky=E)
        dic['DX'], dic['BX'] = dic['BX'], dic['DX']


    if first_registery == 'CX' and secondregistery == 'DX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=5, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=4, sticky=E)
        dic['DX'], dic['CX'] = dic['CX'], dic['DX']


    if first_registery == 'DX' and secondregistery == 'CX':
        ttk.Label(mainframe, text=dic[first_registery], width = 20).grid(column=2, row=4, sticky= E)
        ttk.Label(mainframe, text=dic[secondregistery], width=20).grid(column=2, row=5, sticky=E)
        dic['DX'], dic['CX'] = dic['CX'], dic['DX']


root = Tk()
root.title("INTEL 8680")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fromTo = StringVar()
meters = StringVar()

from_entry = ttk.Entry(mainframe, width=7, textvariable=fromTo)

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="use format AXBX").grid(column=1, row=1, sticky=W)
from_entry.grid(column=2, row=1, sticky= E)


ttk.Button(mainframe, text="MOV", command = mov).grid(column=5, row=1, sticky=W)
ttk.Button(mainframe, text="SWAP", command = swap).grid(column=6, row=1, sticky=W)


#AX
dic = {
    "AX": '0001011001111110',
    "AL": '00000010', 
    "AH" : '01111110',
    "BX" : '0001000000010100',
    "BL" : '00010100',
    "BH" : '00010100',
    "CX" : '0001111000110110',
    "CL" : '00011110',
    "CH" : '00110110',
    "DX": '0111011000110110', 
    "DH" : '11010110',
    "DL" : '00110110'
    }


AX = StringVar()
AH = StringVar()
AL = StringVar()
BX = StringVar()
BH = StringVar()
BL = StringVar()
CX = StringVar()
CH = StringVar()
CL = StringVar()
DX = StringVar()
DH = StringVar()
DL = StringVar()

A = StringVar()

#AX
ttk.Label(mainframe, text="AX").grid(column=1, row=2, sticky=E)
ttk.Entry(mainframe, textvariable=AX).grid(column=2, row=2, sticky= E)

#BX
ttk.Label(mainframe, text="BX").grid(column=1, row=3, sticky=E)

ttk.Entry(mainframe, textvariable=BX).grid(column=2, row=3, sticky= E)
#CX
ttk.Label(mainframe, text="CX").grid(column=1, row=4, sticky=E )

ttk.Entry(mainframe, textvariable=CX).grid(column=2, row=4, sticky= E)

#DX
ttk.Label(mainframe, text="DX").grid(column=1, row=5, sticky=E)

ttk.Entry(mainframe, textvariable=DX).grid(column=2, row=5, sticky= E)

def enter_values():
    ttk.Label(mainframe, text= AX.get(), width=20).grid(column = 2, row = 2)
    ttk.Label(mainframe, text= BX.get(), width=20).grid(column = 2, row = 3)
    ttk.Label(mainframe, text= CX.get(), width=20).grid(column = 2, row = 4)
    ttk.Label(mainframe, text= DX.get(), width=20).grid(column = 2, row = 5)

    dic['AX'] = AX.get()
    dic['AH'] = AX.get()[:int(len(dic['AX'])/2)]
    dic['AL'] = AX.get()[int(len(dic['AX'])/2):]

    dic['BX'] = BX.get()
    dic['BH'] = BX.get()[:int(len(dic['BX']) / 2)]
    dic['BL'] = BX.get()[int(len(dic['BX']) / 2):]

    dic['CX'] = CX.get()
    dic['CH'] = CX.get()[:int(len(dic['CX']) / 2)]
    dic['CL'] = CX.get()[int(len(dic['CX']) / 2):]

    dic['DX'] = DX.get()
    dic['DH'] = DX.get()[:int(len(dic['DX']) / 2)]
    dic['DL'] = DX.get()[int(len(dic['DX']) / 2):]

ttk.Button(mainframe, text="Enter values", command = enter_values).grid(column=6, row=7, sticky=E)



root.mainloop()