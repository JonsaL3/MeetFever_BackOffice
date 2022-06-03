import tkinter as tk
import webservice.web_service_experiencia as wse

from tkinter import ttk, messagebox
from model.Experiencia import Experiencia


class UpdateInsertExperiencias:

    def __init__(self, experiencia: Experiencia):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar experiencia.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)

        # Datos que necesito
        self.experiencia = experiencia
        self.Id = tk.StringVar(self.ventana)
        self.Titulo = tk.StringVar(self.ventana)
        self.Descripcion = tk.StringVar(self.ventana)
        self.Fecha_Celebracion = tk.StringVar(self.ventana)
        self.Precio = tk.StringVar(self.ventana)
        self.Aforo = tk.StringVar(self.ventana)
        self.Foto = tk.StringVar(self.ventana)
        self.Id_Empresa = tk.StringVar(self.ventana)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.experiencia_gui.manage_experiencias_gui import ExperienciasGui
            self.ventana.destroy()
            ExperienciasGui().iniciar_ventana()

    def cargar_widgets(self):
        # Id
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.experiencia is not None:
            id_entry.insert(0, self.experiencia.Id)
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Titulo
        ttk.Label(self.ventana, text="Título: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        titulo_entry = ttk.Entry(self.ventana, textvariable=self.Titulo, font=self.font)
        if self.experiencia is not None:
            titulo_entry.insert(0, self.experiencia.Titulo)
        titulo_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Descripcion
        ttk.Label(self.ventana, text="Descripción: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        descripcion_entry = ttk.Entry(self.ventana, textvariable=self.Descripcion, font=self.font)
        if self.experiencia is not None:
            descripcion_entry.insert(0, self.experiencia.Descripcion)
        descripcion_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Fecha celebracion
        ttk.Label(self.ventana, text="Fecha celebración: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        fecha_celebracion_entry = ttk.Entry(self.ventana, textvariable=self.Fecha_Celebracion, font=self.font)
        if self.experiencia is not None:
            fecha_celebracion_entry.insert(0, self.experiencia.Fecha_Celebracion)
        fecha_celebracion_entry.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # Precio
        ttk.Label(self.ventana, text="Precio: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        precio_entry = ttk.Entry(self.ventana, textvariable=self.Precio, font=self.font)
        if self.experiencia is not None:
            precio_entry.insert(0, self.experiencia.Precio)
        precio_entry.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

        # Aforo
        ttk.Label(self.ventana, text="Aforo: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        aforo_entry = ttk.Entry(self.ventana, textvariable=self.Aforo, font=self.font)
        if self.experiencia is not None:
            aforo_entry.insert(0, self.experiencia.Aforo)
        aforo_entry.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la empresa
        ttk.Label(self.ventana, text="Id de la empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        id_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Id_Empresa, font=self.font)
        if self.experiencia is not None:
            id_empresa_entry.insert(0, self.experiencia.Empresa.Id)
        id_empresa_entry.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

        # Botón para actualizar
        ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=14, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)

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
        from gui.experiencia_gui.manage_experiencias_gui import ExperienciasGui

        nueva_experiencia = Experiencia(
            Id=None,
            Aforo=self.Aforo.get(),
            Descripcion=self.Descripcion.get(),
            Fecha_Celebracion=self.Fecha_Celebracion.get(),
            Foto=self.Foto.get(),
            Precio=self.Precio.get(),
            Titulo=self.Titulo.get(),
        )

        if self.experiencia is None:
            if wse.insertar_experiencia(nueva_experiencia):
                messagebox.showinfo("Insertado", "Experiencia insertada correctamente.")
                self.ventana.destroy()
                ExperienciasGui().iniciar_ventana()
        else:
            if wse.actualizar_experiencia(nueva_experiencia):
                messagebox.showinfo("Actualizado", "Experiencia actualizada correctamente.")
                self.ventana.destroy()
                ExperienciasGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
