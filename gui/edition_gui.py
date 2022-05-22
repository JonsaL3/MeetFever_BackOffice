import tkinter
import base64

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

import webservice.web_service_empresa as wse
from model.Empresa import Empresa

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def relative_to_assets(path: str) -> Path:
    print(ASSETS_PATH / Path(path))
    return ASSETS_PATH / Path(path)


class EditionGui:

    def __init__(self, type: str):
        # La ventana en si
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#F4F4F4")
        self.window.resizable(False, False)

        # Elementos que la componen
        self.canvas = None
        self.image_image_1 = None
        self.image_1 = None

        # inicializo esos elementos
        self.load_ui_common()
        self.load_ui_specific(type)

    def load_ui_common(self):
        self.canvas = Canvas(
            self.window,
            bg="#F4F4F4",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            640.0,
            360.0,
            image=self.image_image_1
        )

    def iniciar_ventana(self):
        self.window.mainloop()

    def load_ui_specific(self, tipo: str):
        print(tipo)
        if tipo == "EMPRESA":
            self.load_ui_empresa()
        elif tipo == "PERSONA":
            self.load_ui_persona()
        elif tipo == "SEXO":
            self.load_ui_sexo()
        elif tipo == "EXPERIENCIA":
            self.load_ui_experiencia()
        elif tipo == "OPINION":
            self.load_ui_opinion()
        elif tipo == "EMOTICONO":
            self.load_ui_emoticono()
        elif tipo == "LOG":
            self.load_ui_log()
        else:
            print("Tipo no reconocido")

    def load_ui_empresa(self):

        # Me descargo todas las empresas
        empresas = wse.get_all_empresas()

        # Pinto el titulo de la empresa
        self.window.title("Empresas")
        self.canvas.create_text(
            457.0,
            45.0,
            anchor="nw",
            text="Administracion de Empresas:",
            fill="#000000",
            font=("ArialMT", 32 * -1)
        )

        # en medio de la ventana principal, debe aparecer un canvas
        frame = ttk.Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # ahora meto cada de las empresas a ese frame
        for i in range(len(empresas)):
            # Asi tengo al empresa a mano
            empresa: Empresa = empresas[i]

            # Por cada empresa me creo un canvas
            canvas = Canvas(
                frame,
                bg="#4158D0",
                height=50,
                width=50,
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )
            canvas.grid(row=i, column=0, pady=10, padx=10)

            ttk.Label(frame, text=empresa.Id).grid(row=i, column=1, pady=10, padx=10)
            ttk.Label(frame, text=empresa.Correo).grid(row=i, column=2, pady=10, padx=10)

            button = ttk.Button(
                frame,
                text="Eliminar",
            )
            button.grid(row=i, column=4, pady=10, padx=10)

    def load_ui_persona(self):
        print("PERSONA")

    def load_ui_sexo(self):
        print("SEXO")

    def load_ui_experiencia(self):
        print("EXPERIENCIA")

    def load_ui_opinion(self):
        print("OPINION")

    def load_ui_emoticono(self):
        print("EMOTICONO")

    def load_ui_log(self):
        print("LOG")
