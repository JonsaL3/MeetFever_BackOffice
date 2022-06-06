import base64
import binascii
import tkinter as tk
from io import BytesIO

import PIL
from PIL import Image, ImageTk

import webservice.web_service_persona as wsp
import webservice.web_service_sexo as wss

from tkinter import ttk, messagebox, filedialog
from model.Persona import Persona
from model.Sexo import Sexo


class UpdateInsertPersona:

    def __init__(self, persona: Persona):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar persona.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)

        # Datos que necesito
        self.persona = persona
        self.Id = tk.StringVar(self.ventana)
        self.Correo = tk.StringVar(self.ventana)
        self.Contrasena = tk.StringVar(self.ventana)
        self.Nick = tk.StringVar(self.ventana)
        self.Telefono = tk.StringVar(self.ventana)
        self.Frase = tk.StringVar(self.ventana)
        self.Foto_Perfil = tk.StringVar(self.ventana)
        self.Foto_Fondo = tk.StringVar(self.ventana)
        self.Dni = tk.StringVar(self.ventana)
        self.Nombre = tk.StringVar(self.ventana)
        self.Apellido1 = tk.StringVar(self.ventana)
        self.Apellido2 = tk.StringVar(self.ventana)
        self.Sexo = tk.StringVar(self.ventana)
        self.Fecha_Nacimiento = tk.StringVar(self.ventana)

        # contenedor perfil
        self.Contenedor_Foto_Perfil = None
        self.Contenedor_Foto_Fondo = None

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Foto por defecto
        self.photo = tk.PhotoImage(file='assets/default_person.png')
        self.photo = self.photo.subsample(2, 2)
        self.label_photo = None
        self.label = None
        self.imagen = None

        # otros
        self.Sexo_Combobox = None
        self.lista_sexos = wss.get_all_sexos()
        self.lista_sexos = [sexo.Sexo for sexo in self.lista_sexos]

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
            try:
                id_entry.insert(0, self.persona.Id)
            except AttributeError:
                id_entry.insert(0, "")
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Correo de la empresa
        ttk.Label(self.ventana, text="Correo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        correo_entry = ttk.Entry(self.ventana, textvariable=self.Correo, font=self.font)
        if self.persona is not None:
            try:
                correo_entry.insert(0, self.persona.Correo)
            except AttributeError:
                correo_entry.insert(0, "")
        correo_entry.grid(row=1, column=1, padx=5, pady=5)

        # Contraseña de la empresa
        ttk.Label(self.ventana, text="Contraseña: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        contrasena_entry = ttk.Entry(self.ventana, textvariable=self.Contrasena, font=self.font)
        if self.persona is not None:
            try:
                contrasena_entry.insert(0, self.persona.Contrasena)
            except AttributeError:
                contrasena_entry.insert(0, "")
        contrasena_entry.grid(row=2, column=1, padx=5, pady=5)

        # Nick de la empresa
        ttk.Label(self.ventana, text="Nick: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        nick_entry = ttk.Entry(self.ventana, textvariable=self.Nick, font=self.font)
        if self.persona is not None:
            try:
                nick_entry.insert(0, self.persona.Nick)
            except AttributeError:
                nick_entry.insert(0, "")
        nick_entry.grid(row=3, column=1, padx=5, pady=5)

        # Telefono de la empresa
        ttk.Label(self.ventana, text="Telefono: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        telefono_entry = ttk.Entry(self.ventana, textvariable=self.Telefono, font=self.font)
        if self.persona is not None:
            try:
                telefono_entry.insert(0, self.persona.Telefono)
            except AttributeError:
                telefono_entry.insert(0, "")
        telefono_entry.grid(row=4, column=1, padx=5, pady=5)

        # Frase de la empresa
        ttk.Label(self.ventana, text="Frase: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        frase_entry = ttk.Entry(self.ventana, textvariable=self.Frase, font=self.font)
        if self.persona is not None:
            try:
                frase_entry.insert(0, self.persona.Frase)
            except AttributeError:
                frase_entry.insert(0, "")
        frase_entry.grid(row=5, column=1, padx=5, pady=5)

        # Nombre de la empresa
        ttk.Label(self.ventana, text="Dni: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        nombre_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Dni, font=self.font)
        if self.persona is not None:
            try:
                nombre_empresa_entry.insert(0, self.persona.Dni)
            except AttributeError:
                nombre_empresa_entry.insert(0, "")
        nombre_empresa_entry.grid(row=6, column=1, padx=5, pady=5)

        # Cif de la empresa
        ttk.Label(self.ventana, text="Nombre: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        cif_entry = ttk.Entry(self.ventana, textvariable=self.Nombre, font=self.font)
        if self.persona is not None:
            try:
                cif_entry.insert(0, self.persona.Nombre)
            except AttributeError:
                cif_entry.insert(0, "")
        cif_entry.grid(row=7, column=1, padx=5, pady=5)

        # Direccion de facturación de la empresa
        ttk.Label(self.ventana, text="Apellido1: ", font=self.font).grid(row=8, column=0, sticky="nsew")
        facturacion_entry = ttk.Entry(self.ventana, textvariable=self.Apellido1, font=self.font)
        if self.persona is not None:
            try:
                facturacion_entry.insert(0, self.persona.Apellido1)
            except AttributeError:
                facturacion_entry.insert(0, "")
        facturacion_entry.grid(row=8, column=1, padx=5, pady=5)

        # Dirección fiscal de la empresa
        ttk.Label(self.ventana, text="Apellido2: ", font=self.font).grid(row=9, column=0, sticky="nsew")
        fiscal_entry = ttk.Entry(self.ventana, textvariable=self.Apellido2, font=self.font)
        if self.persona is not None:
            try:
                fiscal_entry.insert(0, self.persona.Apellido2)
            except AttributeError:
                fiscal_entry.insert(0, "")
        fiscal_entry.grid(row=9, column=1, padx=5, pady=5)

        # Nombre de la persona fisica
        ttk.Label(self.ventana, text="Fecha Nacimiento: ", font=self.font).grid(row=10, column=0, sticky="nsew")
        persona_fisica = ttk.Entry(self.ventana, textvariable=self.Fecha_Nacimiento, font=self.font)
        if self.persona is not None:
            try:
                persona_fisica.insert(0, self.persona.Fecha_Nacimiento)
            except AttributeError:
                persona_fisica.insert(0, "")
        persona_fisica.grid(row=10, column=1, padx=5, pady=5)

        # Me descargo la lista de sexos y la meto en un combobox:
        ttk.Label(self.ventana, text="Sexo: ", font=self.font).grid(row=11, column=0, sticky="nsew")
        self.Sexo = tk.StringVar()
        self.Sexo.set(self.persona.Sexo.Sexo)
        self.Sexo_Combobox = ttk.Combobox(self.ventana, textvariable=self.Sexo, state="readonly")
        self.Sexo_Combobox.grid(row=11, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.Sexo_Combobox.config(values=self.lista_sexos)

        # Cambiar imagen perfil
        ttk.Label(self.ventana, text="Foto de perfil: ", font=self.font).grid(row=12, column=0, sticky="nsew")
        if self.persona is not None:
            try:
                img = Image.open(BytesIO(base64.b64decode(self.persona.Foto_Perfil)))
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=img)
                self.Contenedor_Foto_Perfil.image = img
                self.Contenedor_Foto_Perfil.grid(row=12, column=1, columnspan=2, sticky="nsew")
                self.Foto_Perfil.set(self.persona.Foto_Perfil)
            except binascii.Error:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=12, column=1, columnspan=2, sticky="nsew")
            except PIL.UnidentifiedImageError:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=12, column=1, columnspan=2, sticky="nsew")
            except AttributeError:
                self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Perfil.config(width=50, height=50)
                self.Contenedor_Foto_Perfil.photo = self.photo
                self.Contenedor_Foto_Perfil.grid(row=12, column=1, columnspan=2, sticky="nsew")
        else:
            self.Contenedor_Foto_Perfil = tk.Label(self.ventana, image=self.photo)
            self.Contenedor_Foto_Perfil.config(width=50, height=50)
            self.Contenedor_Foto_Perfil.photo = self.photo
            self.Contenedor_Foto_Perfil.grid(row=12, column=1, columnspan=2, sticky="nsew")

        ttk.Button(self.ventana, text="Cambiar Foto de perfil", command=lambda: {
            self.obtener_imagen_de_equipo(self.Foto_Perfil, 12, 1, self.Contenedor_Foto_Perfil)
        }).grid(row=13, column=1)

        # Cambiar la foto de fondo:
        ttk.Label(self.ventana, text="Foto de fondo: ", font=self.font).grid(row=13, column=0, sticky="nsew")
        if self.persona is not None:
            try:
                img = Image.open(BytesIO(base64.b64decode(self.persona.Foto_Fondo)))
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=img)
                self.Contenedor_Foto_Fondo.image = img
                self.Contenedor_Foto_Fondo.grid(row=14, column=1, columnspan=2, sticky="nsew")
                self.Foto_Fondo.set(self.persona.Foto_Fondo)
            except binascii.Error:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=14, column=1, columnspan=2, sticky="nsew")
            except PIL.UnidentifiedImageError:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=14, column=1, columnspan=2, sticky="nsew")
            except AttributeError:
                self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto_Fondo.config(width=50, height=50)
                self.Contenedor_Foto_Fondo.photo = self.photo
                self.Contenedor_Foto_Fondo.grid(row=14, column=1, columnspan=2, sticky="nsew")
        else:
            self.Contenedor_Foto_Fondo = tk.Label(self.ventana, image=self.photo)
            self.Contenedor_Foto_Fondo.config(width=50, height=50)
            self.Contenedor_Foto_Fondo.photo = self.photo
            self.Contenedor_Foto_Fondo.grid(row=14, column=1, columnspan=2, sticky="nsew")

        ttk.Button(self.ventana, text="Cambiar Foto de fondo", command=lambda: {
            self.obtener_imagen_de_equipo(self.Foto_Fondo, 14, 1, self.Contenedor_Foto_Fondo)
        }).grid(row=15, column=1)

        # Botón para actualizar
        if self.persona is not None:
            ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=16, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)
        else:
            ttk.Button(self.ventana, text="Insertar", command=self.actualizar_insertar).grid(row=16, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)

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

        sexo_a_enviar = None

        for sexo in wss.get_all_sexos():
            print(sexo)
            if sexo.Sexo == self.Sexo.get():
                sexo_a_enviar = Sexo(sexo.Id, sexo.Sexo)
                break

        nueva_persona = Persona(
            id=self.Id.get(),
            correo=self.Correo.get(),
            contrasena=self.Contrasena.get(),
            nick=self.Nick.get(),
            foto_perfil=self.Foto_Perfil.get(),
            foto_fondo=self.Foto_Fondo.get(),
            telefono=self.Telefono.get(),
            frase=self.Frase.get(),
            Dni=self.Dni.get(),
            Nombre=self.Nombre.get(),
            Apellido1=self.Apellido1.get(),
            Apellido2=self.Apellido2.get(),
            Fecha_Nacimiento=self.Fecha_Nacimiento.get(),
            Sexo=sexo_a_enviar,
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