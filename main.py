# jelszógenerátor
from fuggveny import *

print(jelszogenerator(15, True, True))

from tkinter import *
import fuggveny
import objektum


def jelszokiiras():
    jelszo_ertek.pack()

p = objektum.Jelszoobjektum()
p.jelszogenerator()
print(p.jelszo)


ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.minsize(width=200, height=100)
jelszo_cimke = Label(ablak, text='A jelszó: ', fg='red')
jelszo_ertek = Label(ablak, text=fuggveny.jelszogenerator(15, True, False))
lezaro_gomb = Button(ablak, text='Lezárás', command=ablak.destroy)
jelszo_gomb = Button(ablak, text='Generálás', command=jelszokiiras)

jelszo_cimke.pack()
jelszo_gomb.pack()
lezaro_gomb.pack()
mainloop()
