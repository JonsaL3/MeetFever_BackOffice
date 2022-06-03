from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

from gui.empresa_gui.manage_empresas_gui import EmpresasGui
from gui.persona_gui.manage_personas_gui import PersonasGui
from gui.opinion_gui.manage_opiniones_gui import OpinionesGui
from gui.experiencia_gui.manage_experiencias_gui import ExperienciasGui
from gui.emoji_gui.manage_emojis_gui import EmojisGui
from gui.sexo_gui.manage_sexos import SexosGui
from gui.log_gui.manage_logs import LogsGui

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
        self.center()
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

    def center(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        frm_width = self.window.winfo_rootx() - self.window.winfo_x()
        win_width = width + 2 * frm_width
        height = self.window.winfo_height()
        titlebar_height = self.window.winfo_rooty() - self.window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.window.winfo_screenwidth() // 2 - win_width // 2
        y = self.window.winfo_screenheight() // 2 - win_height // 2
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def cargar_ventana_empresa(self):
        self.window.destroy()
        EmpresasGui().iniciar_ventana()

    def cargar_ventana_persona(self):
        self.window.destroy()
        PersonasGui().iniciar_ventana()

    def cargar_ventana_sexo(self):
        self.window.destroy()
        SexosGui().iniciar_ventana()

    def cargar_ventana_experiencia(self):
        self.window.destroy()
        ExperienciasGui().iniciar_ventana()

    def cargar_venana_emoji(self):
        self.window.destroy()
        EmojisGui().iniciar_ventana()

    def cargar_ventana_log(self):
        self.window.destroy()
        LogsGui().iniciar_ventana()

    def cargar_ventana_opinion(self):
        self.window.destroy()
        OpinionesGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.window.mainloop()

    def cerrar_sesion(self):
        self.window.destroy()
        from gui.login_gui import LoginGui
        LoginGui().iniciar_ventana()

    def salir(self):
        self.window.destroy()

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
            command=lambda: self.cargar_ventana_experiencia(),
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
            command=lambda: self.cargar_venana_emoji(),
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
            command=lambda: self.salir(),
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
            command=lambda: self.cerrar_sesion(),
            relief="flat"
        )
        self.button_9.place(
            x=1051.880859375,
            y=640.7948608398438,
            width=172.149169921875,
            height=40.80340576171875
        )
