import tkinter as tk
import webservice.web_service_empresa as wse

from tkinter import ttk, messagebox
from model.Empresa import Empresa


class UpdateInsertEmpresa:

    def __init__(self, empresa: Empresa):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar empresa.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)

        # Datos que necesito
        self.empresa = empresa
        self.Id = tk.StringVar(self.ventana)
        self.Correo = tk.StringVar(self.ventana)
        self.Contrasena = tk.StringVar(self.ventana)
        self.Nick = tk.StringVar(self.ventana)
        # TODO FOTO PERFIL
        # TODO FOTO FONDO
        self.Telefono = tk.StringVar(self.ventana)
        self.Frase = tk.StringVar(self.ventana)
        self.Nombre_Empresa = tk.StringVar(self.ventana)
        self.Cif = tk.StringVar(self.ventana)
        self.Direccion_Facturacion = tk.StringVar(self.ventana)
        self.Direccion_Fiscal = tk.StringVar(self.ventana)
        self.Nombre_Persona = tk.StringVar(self.ventana)
        self.Apellido1_Persona = tk.StringVar(self.ventana)
        self.Apellido2_Persona = tk.StringVar(self.ventana)
        self.Dni_Persona = tk.StringVar(self.ventana)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.empresa_gui.manage_empresas_gui import EmpresasGui
            self.ventana.destroy()
            EmpresasGui().iniciar_ventana()

    def cargar_widgets(self):
        # Id de la empresa
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.empresa is not None:
            id_entry.insert(0, self.empresa.Id)
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Correo de la empresa
        ttk.Label(self.ventana, text="Correo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        correo_entry = ttk.Entry(self.ventana, textvariable=self.Correo, font=self.font)
        if self.empresa is not None:
            correo_entry.insert(0, self.empresa.Correo)
        correo_entry.grid(row=1, column=1, padx=5, pady=5)

        # Contraseña de la empresa
        ttk.Label(self.ventana, text="Contraseña: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        contrasena_entry = ttk.Entry(self.ventana, textvariable=self.Contrasena, font=self.font)
        if self.empresa is not None:
            contrasena_entry.insert(0, self.empresa.Contrasena)
        contrasena_entry.grid(row=2, column=1, padx=5, pady=5)

        # Nick de la empresa
        ttk.Label(self.ventana, text="Nick: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        nick_entry = ttk.Entry(self.ventana, textvariable=self.Nick, font=self.font)
        if self.empresa is not None:
            nick_entry.insert(0, self.empresa.Nick)
        nick_entry.grid(row=3, column=1, padx=5, pady=5)

        # Telefono de la empresa
        ttk.Label(self.ventana, text="Telefono: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        telefono_entry = ttk.Entry(self.ventana, textvariable=self.Telefono, font=self.font)
        if self.empresa is not None:
            telefono_entry.insert(0, self.empresa.Telefono)
        telefono_entry.grid(row=4, column=1, padx=5, pady=5)

        # Frase de la empresa
        ttk.Label(self.ventana, text="Frase: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        frase_entry = ttk.Entry(self.ventana, textvariable=self.Frase, font=self.font)
        if self.empresa is not None:
            frase_entry.insert(0, self.empresa.Frase)
        frase_entry.grid(row=5, column=1, padx=5, pady=5)

        # Nombre de la empresa
        ttk.Label(self.ventana, text="Nombre Empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        nombre_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Nombre_Empresa, font=self.font)
        if self.empresa is not None:
            nombre_empresa_entry.insert(0, self.empresa.Nombre_Empresa)
        nombre_empresa_entry.grid(row=6, column=1, padx=5, pady=5)

        # Cif de la empresa
        ttk.Label(self.ventana, text="Cif: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        cif_entry = ttk.Entry(self.ventana, textvariable=self.Cif, font=self.font)
        if self.empresa is not None:
            cif_entry.insert(0, self.empresa.Cif)
        cif_entry.grid(row=7, column=1, padx=5, pady=5)

        # Direccion de facturación de la empresa
        ttk.Label(self.ventana, text="Direccion Facturacion: ", font=self.font).grid(row=8, column=0, sticky="nsew")
        facturacion_entry = ttk.Entry(self.ventana, textvariable=self.Direccion_Facturacion, font=self.font)
        if self.empresa is not None:
            facturacion_entry.insert(0, self.empresa.Direccion_Facturacion)
        facturacion_entry.grid(row=8, column=1, padx=5, pady=5)

        # Dirección fiscal de la empresa
        ttk.Label(self.ventana, text="Direccion Fiscal: ", font=self.font).grid(row=9, column=0, sticky="nsew")
        fiscal_entry = ttk.Entry(self.ventana, textvariable=self.Direccion_Fiscal, font=self.font)
        if self.empresa is not None:
            fiscal_entry.insert(0, self.empresa.Direccion_Fiscal)
        fiscal_entry.grid(row=9, column=1, padx=5, pady=5)

        # Nombre de la persona fisica
        ttk.Label(self.ventana, text="Nombre Persona: ", font=self.font).grid(row=10, column=0, sticky="nsew")
        persona_fisica = ttk.Entry(self.ventana, textvariable=self.Nombre_Persona, font=self.font)
        if self.empresa is not None:
            persona_fisica.insert(0, self.empresa.Nombre_Persona)
        persona_fisica.grid(row=10, column=1, padx=5, pady=5)

        # Apellido 1 de la persona fisica
        ttk.Label(self.ventana, text="Apellido 1 Persona: ", font=self.font).grid(row=11, column=0, sticky="nsew")
        apellido1_entry = ttk.Entry(self.ventana, textvariable=self.Apellido1_Persona, font=self.font)
        if self.empresa is not None:
            apellido1_entry.insert(0, self.empresa.Apellido1_Persona)
        apellido1_entry.grid(row=11, column=1, padx=5, pady=5)

        # Apellido 2 de la persona fisica
        ttk.Label(self.ventana, text="Apellido 2 Persona: ", font=self.font).grid(row=12, column=0, sticky="nsew")
        apellido2_entry = ttk.Entry(self.ventana, textvariable=self.Apellido2_Persona, font=self.font)
        if self.empresa is not None:
            apellido2_entry.insert(0, self.empresa.Apellido2_Persona)
        apellido2_entry.grid(row=12, column=1, padx=5, pady=5)

        # Dni de la persona fisica
        ttk.Label(self.ventana, text="Dni Persona: ", font=self.font).grid(row=13, column=0, sticky="nsew")
        dni_entry = ttk.Entry(self.ventana, textvariable=self.Dni_Persona, font=self.font)
        if self.empresa is not None:
            dni_entry.insert(0, self.empresa.Dni_Persona)
        dni_entry.grid(row=13, column=1, padx=5, pady=5)

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
        from gui.empresa_gui.manage_empresas_gui import EmpresasGui

        nueva_empresa = Empresa(
                    id=self.Id.get(),
                    correo=self.Correo.get(),
                    contrasena=self.Contrasena.get(),
                    nick=self.Nick.get(),
                    foto_perfil="",  # TODO,
                    foto_fondo="",  # TODO
                    telefono=self.Telefono.get(),
                    frase=self.Frase.get(),
                    nombre_empresa=self.Nombre_Empresa.get(),
                    cif=self.Cif.get(),
                    direccion_facturacion=self.Direccion_Facturacion.get(),
                    direccion_fiscal=self.Direccion_Fiscal.get(),
                    nombre_persona=self.Nombre_Persona.get(),
                    apellido1_persona=self.Apellido1_Persona.get(),
                    apellido2_persona=self.Apellido2_Persona.get(),
                    dni_persona=self.Dni_Persona.get()
                )

        if self.empresa is None:
            if wse.insert_empresa(nueva_empresa):
                messagebox.showinfo("Insertado", "Empresa insertada correctamente.")
                self.ventana.destroy()
                EmpresasGui().iniciar_ventana()
        else:
            if wse.update_empresa(nueva_empresa):
                messagebox.showinfo("Actualizado", "Empresa actualizada correctamente.")
                self.ventana.destroy()
                EmpresasGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
