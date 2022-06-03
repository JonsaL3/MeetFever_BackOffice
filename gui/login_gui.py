import hashlib
import tkinter

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
from gui.main_gui import MainGui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../login_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_csv_from_file() -> list:
    ruta_imagen = filedialog.askopenfilename(initialdir="/", title="Seleccione una imagen", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    with open(relative_to_assets(ruta_imagen), "r") as file:
        keys = file.read().split(";")
        return keys


class LoginGui:

    def __init__(self):
        # la ventana asi
        self.window = Tk()
        self.window.geometry("1280x720")
        self.center()
        self.window.configure(bg="#F4F4F4")
        self.window.resizable(False, False)

        # Datos que necesito
        self.keys: list = None
        self.usuario: tkinter.StringVar = tkinter.StringVar()
        self.contrasena: tkinter.StringVar = tkinter.StringVar()
        self.font = ("Montserrat Light", 12)

        # Elementos que necesito
        self.canvas = None
        self.entry_2 = None
        self.entry_image_2 = None
        self.entry_1 = None
        self.entry_image_1 = None
        self.image_image_1 = None
        self.button_image_1 = None
        self.button_1 = None
        self.button_2 = None
        self.image_1 = None
        self.button_image_2 = None

        # Cara de elementos graficos
        self.cargar_widgets()

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

    def buscar_creedenciales(self):
        self.keys = get_csv_from_file()

    def iniciar_sesion(self):
        if self.keys is not None:
            usuarioMD5 = hashlib.md5(self.usuario.get().encode("utf-8")).hexdigest()
            contrasenaMD5 = hashlib.md5(self.contrasena.get().encode("utf-8")).hexdigest()
            if usuarioMD5 in self.keys and contrasenaMD5 in self.keys:
                self.window.destroy()
                MainGui().iniciar_ventana()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        else:
            messagebox.showerror("Error", "Debe de importar el fichero de credenciales.")

    def iniciar_ventana(self):
        self.window.mainloop()

    def cargar_widgets(self):
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
            639.0,
            360.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            994.0,
            353.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.usuario,
            font=self.font,
        )
        self.entry_1.place(
            x=809.5,
            y=330.0,
            width=369.0,
            height=45.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            994.0,
            475.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.contrasena,
            show="*",
            font=self.font
        )
        self.entry_2.place(
            x=809.5,
            y=452.0,
            width=369.0,
            height=45.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.iniciar_sesion(),
            relief="flat"
        )
        self.button_1.place(
            x=817.0,
            y=544.0,
            width=172.0,
            height=52.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.buscar_creedenciales(),
            relief="flat"
        )
        self.button_2.place(
            x=999.0,
            y=544.0,
            width=172.0,
            height=52.0
        )
