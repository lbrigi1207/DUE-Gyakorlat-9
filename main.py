#JELSZÓGENERÁTOR
#Véletlenszerűen geenrálunk jelszót
#meghatározott hosszúságú legyen
#először betük, aztán számjegyek, és írásjelek

'''import fuggveny
print(fuggveny.jelszogenerator(8, True, True))

import objektum

p = objektum.Jelszoobjektum()
print(p.jelszogenerator())
'''

from tkinter import *
import fuggveny

def jelszokiiras():
    jelszo_cimke.pack()

ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.minsize(300, 200)
cimke = Label(ablak, text='Jelszó: ', fg='red')
jelszo_cimke = Label(ablak, text=fuggveny.jelszogenerator(10, True, True))
ok_gomb = Button(ablak, text='OK', command=ablak.destroy)
jelszo_gomb = Button(ablak, text='Jelszógenerálás', command=jelszokiiras())

cimke.pack()
ok_gomb.pack()
jelszo_gomb.pack()

mainloop()
