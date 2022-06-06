import base64
import binascii
import tkinter as tk
import webservice.web_service_emoticono as wse
import PIL

from io import BytesIO
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
from model.Emoticono import Emoticono


class UpdateInsertEmoji:

    def __init__(self, emoticono: Emoticono):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar emoticono.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)
        self.ventana.geometry("270x300")
        # Elementos que necesito
        self.emoticono_label = None

        # Datos que necesito
        self.emoticono = emoticono
        self.Id = tk.StringVar(self.ventana)
        self.Emoji = tk.StringVar(self.ventana)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.emoji_gui.manage_emojis_gui import EmojisGui
            self.ventana.destroy()
            EmojisGui().iniciar_ventana()

    def cargar_widgets(self):

        # Emoticono en si
        if self.emoticono is not None:
            try:
                # pinto el emoticono
                img = Image.open(BytesIO(base64.b64decode(self.emoticono.Emoji)))
                img = img.resize((100, 100), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.emoticono_label = tk.Label(self.ventana, image=img)
                self.emoticono_label.image = img
                self.emoticono_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
            except binascii.Error:
                print("No se pudo cargar la imagen de fondo")
            except PIL.UnidentifiedImageError:
                print("No se pudo cargar la imagen de fondo")

        ttk.Button(self.ventana, text="Buscar emoticono...", command=self.obtener_imagen_de_equipo).grid(row=1, column=0, sticky="nsew", columnspan=2, padx=20, pady=20)

        # Id de la empresa
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.emoticono is not None:
            id_entry.insert(0, str(self.emoticono.Id))
        id_entry.config(state="readonly")
        id_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Botón para actualizar
        ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=3, column=0, sticky="nsew", padx=20, pady=20, columnspan=2)
        self.center()

    def obtener_imagen_de_equipo(self):
        ruta_imagen = filedialog.askopenfilename(initialdir="/", title="Seleccione una imagen", filetypes=(("Imagenes", "*.png"), ("Imagenes", "*.jpg"), ("Imagenes", "*.jpeg")))
        if ruta_imagen != "":
            try:
                img = Image.open(ruta_imagen)
                img = img.resize((100, 100), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.emoticono_label = tk.Label(self.ventana, image=img)
                self.emoticono_label.config(image=img)
                self.emoticono_label.image = img
                self.emoticono_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
                # Lo guardo como base 64
                with open(ruta_imagen, "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                    self.Emoji.set(my_string.decode("utf-8"))
            except binascii.Error:
                print("No se pudo cargar la imagen de fondo")

    def center(self):
        self.ventana.update_idletasks()
        width = self.ventana.winfo_width()
        frm_width = self.ventana.winfo_rootx() - self.ventana.winfo_x()
        win_width = width + 2 * frm_width
        height = self.ventana.winfo_height()
        titlebar_height = self.ventana.winfo_rooty() - self.ventana.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.ventana.winfo_screenwidth() // 2 - win_width // 2
        y = self.ventana.winfo_screenheight() // 2 - win_height // 2
        self.ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def actualizar_insertar(self):

        # Lo importo aqui para evitar circular imports
        from gui.emoji_gui.manage_emojis_gui import EmojisGui

        nuevo_emoticono: Emoticono

        if self.emoticono is None:
            nuevo_emoticono = Emoticono(None, self.Emoji.get())
        else:
            nuevo_emoticono = Emoticono(int(self.Id.get()), self.Emoji.get())

        if self.emoticono is None:
            if wse.insertar_emoticono(nuevo_emoticono):
                messagebox.showinfo("Insertado", "Emoji insertado correctamente.")
                self.ventana.destroy()
                EmojisGui().iniciar_ventana()
        else:
            if wse.actualizar_emoticono(nuevo_emoticono):
                messagebox.showinfo("Actualizado", "Emoji actualizado correctamente.")
                self.ventana.destroy()
                EmojisGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
