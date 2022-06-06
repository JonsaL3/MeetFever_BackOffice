import base64
import binascii
import tkinter as tk
from io import BytesIO

import PIL
from PIL import Image, ImageTk

import webservice.web_service_empresa as wse

from tkinter import ttk, messagebox, filedialog
from model.Empresa import Empresa


class UpdateInsertEmpresa:

    def __init__(self, empresa: Empresa):

        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar empresa.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)

        # Datos que necesito
        self.empresa = empresa
        self.Id = tk.StringVar(self.ventana)
        self.Correo = tk.StringVar(self.ventana)
        self.Contrasena = tk.StringVar(self.ventana)
        self.Nick = tk.StringVar(self.ventana)
        self.Foto_Perfil = tk.StringVar(self.ventana)
        self.Foto_Fondo = tk.StringVar(self.ventana)
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

        # Foto por defecto
        self.photo = tk.PhotoImage(file='assets/default_enterprise.png')
        self.photo = self.photo.subsample(2, 2)
        self.label_photo = None
        self.label = None
        self.imagen = None

        # contenedor perfil
        self.Contenedor_Foto_Perfil = None
        self.Contenedor_Foto_Fondo = None

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
            try:
                id_entry.insert(0, self.empresa.Id)
            except AttributeError:
                id_entry.insert(0, "")
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Correo de la empresa
        ttk.Label(self.ventana, text="Correo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        correo_entry = ttk.Entry(self.ventana, textvariable=self.Correo, font=self.font)
        if self.empresa is not None:
            try:
                correo_entry.insert(0, self.empresa.Correo)
            except AttributeError:
                correo_entry.insert(0, "")
        correo_entry.grid(row=1, column=1, padx=5, pady=5)

        # Contraseña de la empresa
        ttk.Label(self.ventana, text="Contraseña: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        contrasena_entry = ttk.Entry(self.ventana, textvariable=self.Contrasena, font=self.font)
        if self.empresa is not None:
            try:
                contrasena_entry.insert(0, self.empresa.Contrasena)
            except AttributeError:
                contrasena_entry.insert(0, "")
        contrasena_entry.grid(row=2, column=1, padx=5, pady=5)

        # Nick de la empresa
        ttk.Label(self.ventana, text="Nick: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        nick_entry = ttk.Entry(self.ventana, textvariable=self.Nick, font=self.font)
        if self.empresa is not None:
            try:
                nick_entry.insert(0, self.empresa.Nick)
            except AttributeError:
                nick_entry.insert(0, "")
        nick_entry.grid(row=3, column=1, padx=5, pady=5)

        # Telefono de la empresa
        ttk.Label(self.ventana, text="Telefono: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        telefono_entry = ttk.Entry(self.ventana, textvariable=self.Telefono, font=self.font)
        if self.empresa is not None:
            try:
                telefono_entry.insert(0, self.empresa.Telefono)
            except AttributeError:
                telefono_entry.insert(0, "")
        telefono_entry.grid(row=4, column=1, padx=5, pady=5)

        # Frase de la empresa
        ttk.Label(self.ventana, text="Frase: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        frase_entry = ttk.Entry(self.ventana, textvariable=self.Frase, font=self.font)
        if self.empresa is not None:
            try:
                frase_entry.insert(0, self.empresa.Frase)
            except AttributeError:
                frase_entry.insert(0, "")
        frase_entry.grid(row=5, column=1, padx=5, pady=5)

        # Nombre de la empresa
        ttk.Label(self.ventana, text="Nombre Empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        nombre_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Nombre_Empresa, font=self.font)
        if self.empresa is not None:
            try:
                nombre_empresa_entry.insert(0, self.empresa.Nombre_Empresa)
            except AttributeError:
                nombre_empresa_entry.insert(0, "")
        nombre_empresa_entry.grid(row=6, column=1, padx=5, pady=5)

        # Cif de la empresa
        ttk.Label(self.ventana, text="Cif: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        cif_entry = ttk.Entry(self.ventana, textvariable=self.Cif, font=self.font)
        if self.empresa is not None:
            try:
                cif_entry.insert(0, self.empresa.Cif)
            except AttributeError:
                cif_entry.insert(0, "")
        cif_entry.grid(row=7, column=1, padx=5, pady=5)

        # Direccion de facturación de la empresa
        ttk.Label(self.ventana, text="Direccion Facturacion: ", font=self.font).grid(row=8, column=0, sticky="nsew")
        facturacion_entry = ttk.Entry(self.ventana, textvariable=self.Direccion_Facturacion, font=self.font)
        if self.empresa is not None:
            try:
                facturacion_entry.insert(0, self.empresa.Direccion_Facturacion)
            except AttributeError:
                facturacion_entry.insert(0, "")
        facturacion_entry.grid(row=8, column=1, padx=5, pady=5)

        # Dirección fiscal de la empresa
        ttk.Label(self.ventana, text="Direccion Fiscal: ", font=self.font).grid(row=9, column=0, sticky="nsew")
        fiscal_entry = ttk.Entry(self.ventana, textvariable=self.Direccion_Fiscal, font=self.font)
        if self.empresa is not None:
            try:
                fiscal_entry.insert(0, self.empresa.Direccion_Fiscal)
            except AttributeError:
                fiscal_entry.insert(0, "")
        fiscal_entry.grid(row=9, column=1, padx=5, pady=5)

        # Nombre de la persona fisica
        ttk.Label(self.ventana, text="Nombre Persona: ", font=self.font).grid(row=10, column=0, sticky="nsew")
        persona_fisica = ttk.Entry(self.ventana, textvariable=self.Nombre_Persona, font=self.font)
        if self.empresa is not None:
            try:
                persona_fisica.insert(0, self.empresa.Nombre_Persona)
            except AttributeError:
                persona_fisica.insert(0, "")
        persona_fisica.grid(row=10, column=1, padx=5, pady=5)

        # Apellido 1 de la persona fisica
        ttk.Label(self.ventana, text="Apellido 1 Persona: ", font=self.font).grid(row=11, column=0, sticky="nsew")
        apellido1_entry = ttk.Entry(self.ventana, textvariable=self.Apellido1_Persona, font=self.font)
        if self.empresa is not None:
            try:
                apellido1_entry.insert(0, self.empresa.Apellido1_Persona)
            except AttributeError:
                apellido1_entry.insert(0, "")
        apellido1_entry.grid(row=11, column=1, padx=5, pady=5)

        # Apellido 2 de la persona fisica
        ttk.Label(self.ventana, text="Apellido 2 Persona: ", font=self.font).grid(row=12, column=0, sticky="nsew")
        apellido2_entry = ttk.Entry(self.ventana, textvariable=self.Apellido2_Persona, font=self.font)
        if self.empresa is not None:
            try:
                apellido2_entry.insert(0, self.empresa.Apellido2_Persona)
            except AttributeError:
                apellido2_entry.insert(0, "")
        apellido2_entry.grid(row=12, column=1, padx=5, pady=5)

        # Dni de la persona fisica
        ttk.Label(self.ventana, text="Dni Persona: ", font=self.font).grid(row=13, column=0, sticky="nsew")
        dni_entry = ttk.Entry(self.ventana, textvariable=self.Dni_Persona, font=self.font)
        if self.empresa is not None:
            try:
                dni_entry.insert(0, self.empresa.Dni_Persona)
            except AttributeError:
                dni_entry.insert(0, "")
        dni_entry.grid(row=13, column=1, padx=5, pady=5)

        # Cambiar imagen perfil
        ttk.Label(self.ventana, text="Foto de perfil: ", font=self.font).grid(row=14, column=0, sticky="nsew")
        if self.empresa is not None:
            try:
                img = Image.open(BytesIO(base64.b64decode(self.empresa.Foto_Perfil)))
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=img)
                self.Contenedor_Foto_Perfil.image = img
                self.Contenedor_Foto_Perfil.grid(row=14, column=1, columnspan=2, sticky="nsew")
                self.Foto_Perfil.set(self.empresa.Foto_Perfil)
            except binascii.Error:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=14, column=1, columnspan=2, sticky="nsew")
            except PIL.UnidentifiedImageError:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=14, column=1, columnspan=2, sticky="nsew")
            except AttributeError:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=14, column=1, columnspan=2, sticky="nsew")
        else:
            self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
            self.Contenedor_Foto_Perfil.config(width=50, height=50)
            self.Contenedor_Foto_Perfil.photo = self.photo
            self.Contenedor_Foto_Perfil.grid(row=14, column=1, columnspan=2, sticky="nsew")

        ttk.Button(self.ventana, text="Cambiar Foto de perfil", command=lambda: {
            self.obtener_imagen_de_equipo(self.Foto_Perfil, 14, 1, self.Contenedor_Foto_Perfil)
        }).grid(row=15, column=1)

        # Cambiar la foto de fondo:
        ttk.Label(self.ventana, text="Foto de fondo: ", font=self.font).grid(row=16, column=0, sticky="nsew")
        if self.empresa is not None:
            try:
                img = Image.open(BytesIO(base64.b64decode(self.empresa.Foto_Fondo)))
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=img)
                self.Contenedor_Foto_Fondo.image = img
                self.Contenedor_Foto_Fondo.grid(row=16, column=1, columnspan=2, sticky="nsew")
                self.Foto_Fondo.set(self.empresa.Foto_Fondo)
            except binascii.Error:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=16, column=1, columnspan=2, sticky="nsew")
            except PIL.UnidentifiedImageError:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=16, column=1, columnspan=2, sticky="nsew")
            except AttributeError:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=16, column=1, columnspan=2, sticky="nsew")
        else:
            self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
            self.Contenedor_Foto_Fondo.config(width=50, height=50)
            self.Contenedor_Foto_Fondo.photo = self.photo
            self.Contenedor_Foto_Fondo.grid(row=16, column=1, columnspan=2, sticky="nsew")

        ttk.Button(self.ventana, text="Cambiar Foto de fondo", command=lambda: {
            self.obtener_imagen_de_equipo(self.Foto_Fondo, 16, 1, self.Contenedor_Foto_Fondo)
        }).grid(row=17, column=1)

        # Botón para actualizar
        if self.empresa is not None:
            ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=18, column=0, padx=5, pady=5, columnspan=2)
        else:
            ttk.Button(self.ventana, text="Insertar", command=self.actualizar_insertar).grid(row=18, column=0, padx=5, pady=5, columnspan=2)

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

    def obtener_imagen_de_equipo(self, stringvar: tk.StringVar, row, column, donde_va):
        ruta_imagen = filedialog.askopenfilename(initialdir="/", title="Seleccione una imagen", filetypes=(("Imagenes", "*.png"), ("Imagenes", "*.jpg"), ("Imagenes", "*.jpeg")))
        if ruta_imagen != "":
            try:
                img = Image.open(ruta_imagen)
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                donde_va.destroy()
                donde_va = tk.Label(self.ventana, image=img)
                donde_va.image = img
                donde_va.grid(row=row, column=column, sticky="nsew")
                # Lo guardo como base 64
                with open(ruta_imagen, "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                    stringvar.set(my_string.decode("utf-8"))
            except binascii.Error:
                print("No se peuede cargar la imagen.")

    def actualizar_insertar(self):

        # Lo importo aqui para evitar circular imports
        from gui.empresa_gui.manage_empresas_gui import EmpresasGui

        nueva_empresa = Empresa(
                    id=self.Id.get(),
                    correo=self.Correo.get(),
                    contrasena=self.Contrasena.get(),
                    nick=self.Nick.get(),
                    foto_perfil=self.Foto_Perfil.get(),
                    foto_fondo=self.Foto_Fondo.get(),
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
