import tkinter as tk
from pathlib import Path

import webservice.web_service_logs as wsl

from tkinter import ttk, messagebox

from model.Log import Log

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../assets")


def relative_to_assets(path: str) -> Path:
    print(ASSETS_PATH / Path(path))
    return ASSETS_PATH / Path(path)


class LogsGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.iconbitmap(relative_to_assets("indytek_logo.ico"))
        self.ventana.title("Administrar logs")
        self.ventana.geometry("1130x720")
        self.center()
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_menu)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.logs = None

        # Elementos que la componen
        self.contenedor = None
        self.scrollable_frame = None
        self.xscrollbar = None
        self.yscrollbar = None
        self.canvas = None

        # inicializo esos elementos
        self.cargar_widgets()

    def volver_a_menu(self):
        from gui.main_gui import MainGui
        self.ventana.destroy()
        MainGui().iniciar_ventana()

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

    def obtener_logs_actualizados(self):
        self.logs: list[Log] = wsl.get_all_logs()
        self.logs.sort(key=lambda x: x.Id)

    def cargar_widgets(self):

        # Creo un conenedor con scroll
        self.contenedor = ttk.Frame(self.ventana)
        self.canvas = tk.Canvas(self.contenedor)
        self.xscrollbar = ttk.Scrollbar(self.contenedor, orient="horizontal", command=self.canvas.xview)
        self.yscrollbar = ttk.Scrollbar(self.contenedor, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)

        # Muestro la lista de empresas en el frame que me he preparado con gird
        self.obtener_logs_actualizados()
        self.pintar_lista_de_logs()

        # Pinto t.odo en el contenedor
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar.pack(side="right", fill="y")
        self.contenedor.pack(expand=True, fill="both")
        self.canvas.pack(fill="both", expand=True)

        # las scrollbars deben verse en el mismo orden que el contenedor
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

    def pintar_lista_de_logs(self):
        # Muestro el nombre de los campos mostrados
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Sexo", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Aplicación", font=self.font).grid(row=0, column=2, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.logs)):

            try:
                ttk.Label(self.scrollable_frame, text=self.logs[i].Id, font=self.font).grid(row=i + 1, column=0, padx=5, pady=5)
            except:
                print("No se ha podido cargar el atributo.")

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.logs[i].Excepcion[0:100], font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
                if self.logs[i].Eliminado:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.logs[i].Aplicacion_Fuente, font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
            except:
                print("No se ha podido cargar el atributo.")

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=10, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_log(iterador)
            })

    def eliminar_log(self, iterador):
        if messagebox.askyesno("Eliminar sexo", "¿Esta seguro que desea este registro realmente? Esto afectará en cascada a los elementos que lo componen..."):
            if wsl.delete_log_by_id(self.logs[iterador].Id):
                self.logs.pop(iterador)
                messagebox.showinfo("Eliminar registro", "El registro ha sido eliminado correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar registro", "No se pudo eliminar el registro.")

    def actualizar_lista(self):
        self.obtener_logs_actualizados()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_logs()

    def iniciar_ventana(self):
        self.ventana.mainloop()
