from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui.manage_empresas_gui import EmpresasGui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def relative_to_assets(path: str) -> Path:
    print(ASSETS_PATH / Path(path))
    return ASSETS_PATH / Path(path)


class MainGui:

    def __init__(self):
        # La ventana en si
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#F4F4F4")
        self.window.resizable(False, False)

        # Elementos que la componen
        self.button_image_9 = None
        self.button_8 = None
        self.button_image_8 = None
        self.button_7 = None
        self.button_image_7 = None
        self.button_6 = None
        self.button_image_6 = None
        self.button_5 = None
        self.button_image_5 = None
        self.button_4 = None
        self.button_image_4 = None
        self.button_3 = None
        self.button_image_3 = None
        self.button_2 = None
        self.button_image_2 = None
        self.button_1 = None
        self.canvas = None
        self.button_image_1 = None
        self.image_image_1 = None
        self.image_1 = None
        self.button_9 = None

        # inicializo esos elementos
        self.load_ui()

    def cargar_ventana_empresa(self):
        self.window.destroy()
        EmpresasGui().iniciar_ventana()

    def cargar_ventana_persona(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def cargar_ventana_sexo(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def cargar_ventana_experiencia(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def cargar_venana_emoji(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def cargar_ventana_log(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def cargar_ventana_opinion(self):
        self.window.destroy()
        # TODO VENTANA DE EDICION

    def iniciar_ventana(self):
        self.window.mainloop()

    def load_ui(self):
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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_empresa(),
            relief="flat"
        )
        self.button_1.place(
            x=27.0,
            y=20.0,
            width=401.4107666015625,
            height=221.5042724609375
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_persona(),
            relief="flat"
        )
        self.button_2.place(
            x=438.85400390625,
            y=20.0,
            width=401.4107666015625,
            height=221.5042724609375
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_opinion(),
            relief="flat"
        )
        self.button_3.place(
            x=849.8192138671875,
            y=20.0,
            width=401.4107666015625,
            height=221.57640075683594
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_venana_emoji(),
            relief="flat"
        )
        self.button_4.place(
            x=438.85400390625,
            y=250.24786376953125,
            width=401.4107666015625,
            height=221.576416015625
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_experiencia(),
            relief="flat"
        )
        self.button_5.place(
            x=27.0,
            y=250.24786376953125,
            width=401.4107666015625,
            height=221.5042724609375
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_sexo(),
            relief="flat"
        )
        self.button_6.place(
            x=850.58935546875,
            y=250.24786376953125,
            width=401.41064453125,
            height=221.57643127441406
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargar_ventana_log(),
            relief="flat"
        )
        self.button_7.place(
            x=438.8953857421875,
            y=480.4957275390625,
            width=401.4107666015625,
            height=221.5042724609375
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=56.1435546875,
            y=640.7948608398438,
            width=171.9468994140625,
            height=40.80340576171875
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_9.place(
            x=1051.880859375,
            y=640.7948608398438,
            width=172.149169921875,
            height=40.80340576171875
        )
