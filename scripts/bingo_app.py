import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from scripts.functions import generar_bolas, sacar_numero

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo")
        self.root.geometry("800x600")

        # Cargar y configurar imagen de fondo
        try:
            self.background_image = Image.open("images/background.png").resize((800, 600))
            self.background_photo = ImageTk.PhotoImage(self.background_image)
        except FileNotFoundError:
            print("Archivo de imagen no encontrado")
            self.background_photo = None

        if self.background_photo:
            self.background_label = tk.Label(root, image=self.background_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame para el contenido del Bingo
        self.bingo_frame = tk.Frame(root, bg='white')
        self.bingo_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Etiqueta para el número actual
        self.numero_label = tk.Label(self.bingo_frame, text="", font=("Helvetica", 72), bg="white")
        self.numero_label.pack(fill=tk.BOTH, expand=True, pady=(50, 0))

        # Lista para los números ya dichos
        self.numeros_dichos = []
        self.numeros_dichos_label = tk.Label(self.bingo_frame, text="", font=("Helvetica", 12), bg="white")
        self.numeros_dichos_label.pack(pady=20)

        # Botón para sacar un nuevo número
        self.new_number_button = tk.Button(self.bingo_frame, text="Sacar número", command=self.sacar_numero_wrapper)
        self.new_number_button.pack(pady=20)

        # Botón para reiniciar el juego
        self.restart_button = tk.Button(self.bingo_frame, text="Reiniciar juego", command=self.reiniciar_juego)
        self.restart_button.place(relx=0, rely=0)  # Colocar en la esquina superior izquierda

        # Banda de noticias
        self.news_index = 0
        self.news = [
            "4 BINGOS, 4 LÍNEAS",
            "Premio Línea: PreRoll Hachile / Vegano",
            "Premio Bingo: ¡PreRoll Premium!",
            "¡Último bingo premio Sorpresa!",
            "¡Suerte a todos los jugadores!"
        ]
        self.news_label = tk.Label(self.bingo_frame, text=self.news[self.news_index], font=("Helvetica", 16), bg="yellow")
        self.news_label.pack(fill=tk.X, pady=20)
        self.update_news()

        # Generar números al inicio
        self.bolas = generar_bolas()

    def sacar_numero_wrapper(self):
        self.bolas, self.numeros_dichos = sacar_numero(self.bolas, self.numeros_dichos, self.numero_label,
                                                       self.numeros_dichos_label, self)

    def update_numeros_dichos(self):
        line_break = 15  # Número de elementos por línea
        lines = [", ".join(map(str, self.numeros_dichos[i:i + line_break])) for i in range(0, len(self.numeros_dichos), line_break)]
        display_text = "\n".join(lines)
        self.numeros_dichos_label.config(text="Números dichos:\n" + display_text)

    def update_news(self):
        self.news_index = (self.news_index + 1) % len(self.news)
        self.news_label.config(text=self.news[self.news_index])
        self.root.after(5000, self.update_news)  # Actualizar cada 5 segundos

    def reiniciar_juego(self):
        self.bolas = generar_bolas()  # Generar una nueva lista de bolas
        self.numeros_dichos = []  # Reiniciar lista de números dichos
        self.numero_label.config(text="")  # Limpiar número actual
        self.numeros_dichos_label.config(text="")  # Limpiar números dichos
        self.news_index = 0  # Reiniciar índice de noticias
        self.news_label.config(text=self.news[self.news_index])  # Mostrar primera noticia
