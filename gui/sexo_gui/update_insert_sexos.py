import tkinter as tk
import webservice.web_service_sexo as wss

from tkinter import ttk, messagebox
from model.Sexo import Sexo


class UpdateInsertSexo:

    def __init__(self, sexo: Sexo):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar experiencia.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)

        # Datos que necesito
        self.sexo = sexo
        self.Id = tk.StringVar(self.ventana)
        self.Sexo = tk.StringVar(self.ventana)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.sexo_gui.manage_sexos import SexosGui
            self.ventana.destroy()
            SexosGui().iniciar_ventana()

    def cargar_widgets(self):
        # Id
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.sexo is not None:
            id_entry.insert(0, str(self.sexo.Id))
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Sexo
        ttk.Label(self.ventana, text="Sexo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        titulo_entry = ttk.Entry(self.ventana, textvariable=self.Sexo, font=self.font)
        if self.sexo is not None:
            titulo_entry.insert(0, self.sexo.Sexo)
        titulo_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Botón para actualizar
        ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=14, column=0,
                                                                                           sticky="nsew", padx=5,
                                                                                           pady=5, columnspan=2)

        self.center()

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
        from gui.sexo_gui.manage_sexos import SexosGui

        if self.sexo is None:
            nuevo_sexo = Sexo(None, self.Sexo.get())
            if wss.insert_sexo(nuevo_sexo):
                messagebox.showinfo("Insertado", "Sexo insertado correctamente.")
                self.ventana.destroy()
                SexosGui().iniciar_ventana()
        else:
            nuevo_sexo = Sexo(self.sexo.Id, self.Sexo.get())
            if wss.update_sexo(nuevo_sexo):
                messagebox.showinfo("Actualizado", "Sexo actualizado correctamente.")
                self.ventana.destroy()
                SexosGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
