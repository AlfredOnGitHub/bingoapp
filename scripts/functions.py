import numpy as np
from tkinter import messagebox

def generar_bolas():
    return np.random.permutation(range(1, 91))

def sacar_numero(bolas, numeros_dichos, numero_label, numeros_dichos_label, bingo_app_instance):
    if len(bolas) == 0:
        messagebox.showinfo("Bingo", "Inicia un nuevo juego o reinicia para sacar más números.")
        return

    numero = bolas[0]
    bolas = np.delete(bolas, 0)
    numeros_dichos.append(numero)
    numero_label.config(text=str(numero))
    bingo_app_instance.update_numeros_dichos()  # Llamar al método sin argumentos adicionales
    
    return bolas, numeros_dichos
