import tkinter as tk
import webservice.web_service_persona as wsp

from tkinter import ttk, messagebox
from model.Persona import Persona
from model.Sexo import Sexo


class UpdateInsertPersona:

    def __init__(self, persona: Persona):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar persona.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)

        # Datos que necesito
        self.persona = persona
        self.Id = tk.StringVar(self.ventana)
        self.Correo = tk.StringVar(self.ventana)
        self.Contrasena = tk.StringVar(self.ventana)
        self.Nick = tk.StringVar(self.ventana)
        self.Telefono = tk.StringVar(self.ventana)
        self.Frase = tk.StringVar(self.ventana)
        # TODO FOTO PERFIL
        # TODO FOTO FONDO
        self.Dni = tk.StringVar(self.ventana)
        self.Nombre = tk.StringVar(self.ventana)
        self.Apellido1 = tk.StringVar(self.ventana)
        self.Apellido2 = tk.StringVar(self.ventana)
        # TODO SEXO
        self.Fecha_Nacimiento = tk.StringVar(self.ventana)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.persona_gui.manage_personas_gui import PersonasGui
            self.ventana.destroy()
            PersonasGui().iniciar_ventana()

    def cargar_widgets(self):
        # Id de la empresa
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.persona is not None:
            id_entry.insert(0, self.persona.Id)
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Correo de la empresa
        ttk.Label(self.ventana, text="Correo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        correo_entry = ttk.Entry(self.ventana, textvariable=self.Correo, font=self.font)
        if self.persona is not None:
            correo_entry.insert(0, self.persona.Correo)
        correo_entry.grid(row=1, column=1, padx=5, pady=5)

        # Contraseña de la empresa
        ttk.Label(self.ventana, text="Contraseña: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        contrasena_entry = ttk.Entry(self.ventana, textvariable=self.Contrasena, font=self.font)
        if self.persona is not None:
            contrasena_entry.insert(0, self.persona.Contrasena)
        contrasena_entry.grid(row=2, column=1, padx=5, pady=5)

        # Nick de la empresa
        ttk.Label(self.ventana, text="Nick: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        nick_entry = ttk.Entry(self.ventana, textvariable=self.Nick, font=self.font)
        if self.persona is not None:
            nick_entry.insert(0, self.persona.Nick)
        nick_entry.grid(row=3, column=1, padx=5, pady=5)

        # Telefono de la empresa
        ttk.Label(self.ventana, text="Telefono: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        telefono_entry = ttk.Entry(self.ventana, textvariable=self.Telefono, font=self.font)
        if self.persona is not None:
            telefono_entry.insert(0, self.persona.Telefono)
        telefono_entry.grid(row=4, column=1, padx=5, pady=5)

        # Frase de la empresa
        ttk.Label(self.ventana, text="Frase: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        frase_entry = ttk.Entry(self.ventana, textvariable=self.Frase, font=self.font)
        if self.persona is not None:
            frase_entry.insert(0, self.persona.Frase)
        frase_entry.grid(row=5, column=1, padx=5, pady=5)

        # Nombre de la empresa
        ttk.Label(self.ventana, text="Dni: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        nombre_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Dni, font=self.font)
        if self.persona is not None:
            nombre_empresa_entry.insert(0, self.persona.Dni)
        nombre_empresa_entry.grid(row=6, column=1, padx=5, pady=5)

        # Cif de la empresa
        ttk.Label(self.ventana, text="Nombre: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        cif_entry = ttk.Entry(self.ventana, textvariable=self.Nombre, font=self.font)
        if self.persona is not None:
            cif_entry.insert(0, self.persona.Nombre)
        cif_entry.grid(row=7, column=1, padx=5, pady=5)

        # Direccion de facturación de la empresa
        ttk.Label(self.ventana, text="Apellido1: ", font=self.font).grid(row=8, column=0, sticky="nsew")
        facturacion_entry = ttk.Entry(self.ventana, textvariable=self.Apellido1, font=self.font)
        if self.persona is not None:
            facturacion_entry.insert(0, self.persona.Apellido1)
        facturacion_entry.grid(row=8, column=1, padx=5, pady=5)

        # Dirección fiscal de la empresa
        ttk.Label(self.ventana, text="Apellido2: ", font=self.font).grid(row=9, column=0, sticky="nsew")
        fiscal_entry = ttk.Entry(self.ventana, textvariable=self.Apellido2, font=self.font)
        if self.persona is not None:
            fiscal_entry.insert(0, self.persona.Apellido2)
        fiscal_entry.grid(row=9, column=1, padx=5, pady=5)

        # Nombre de la persona fisica
        ttk.Label(self.ventana, text="Fecha Nacimiento: ", font=self.font).grid(row=10, column=0, sticky="nsew")
        persona_fisica = ttk.Entry(self.ventana, textvariable=self.Fecha_Nacimiento, font=self.font)
        if self.persona is not None:
            persona_fisica.insert(0, self.persona.Fecha_Nacimiento)
        persona_fisica.grid(row=10, column=1, padx=5, pady=5)

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
        from gui.persona_gui.manage_personas_gui import PersonasGui

        nueva_persona = Persona(
            id=self.Id.get(),
            correo=self.Correo.get(),
            contrasena=self.Contrasena.get(),
            nick=self.Nick.get(),
            foto_perfil="",  # TODO,
            foto_fondo="",  # TODO
            telefono=self.Telefono.get(),
            frase=self.Frase.get(),
            Dni=self.Dni.get(),
            Nombre=self.Nombre.get(),
            Apellido1=self.Apellido1.get(),
            Apellido2=self.Apellido2.get(),
            Fecha_Nacimiento=self.Fecha_Nacimiento.get(),
            Sexo=Sexo(1, "Hombre")  # TODO
        )

        if self.persona is None:
            if wsp.insert_persona(nueva_persona):
                messagebox.showinfo("Insertado", "Persona insertada correctamente.")
                self.ventana.destroy()
                PersonasGui().iniciar_ventana()
        else:
            if wsp.update_persona(nueva_persona):
                messagebox.showinfo("Actualizado", "Persona actualizada correctamente.")
                self.ventana.destroy()
                PersonasGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
