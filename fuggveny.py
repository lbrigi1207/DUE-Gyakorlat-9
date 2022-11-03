import random
import string

def jelszogenerator(jelszohossz, kell_szamjegy, kell_irasjel ): #paraméterként használva
    jelszo = ''
    karakter_lista = string.ascii_letters
    if kell_szamjegy:
        karakter_lista += string.digits

    if kell_irasjel:
        karakter_lista += string.punctuation

    for _ in range(jelszohossz):  # _ = i
        karakter = karakter_lista[random.randint(0, len(karakter_lista) - 1)]
        jelszo += karakter
    return jelszo

#if __name__ == '__main__':