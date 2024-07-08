import tkinter as tk
from scripts.bingo_app import BingoApp

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()