import base64
import binascii
import tkinter as tk
from io import BytesIO

import PIL
from PIL import Image, ImageTk

import webservice.web_service_experiencia as wse

from tkinter import ttk, messagebox, filedialog

from model.Empresa import Empresa
from model.Experiencia import Experiencia


class UpdateInsertExperiencias:

    def __init__(self, experiencia: Experiencia):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar experiencia.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)

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

        # Foto por defecto
        self.photo = tk.PhotoImage(file='assets/default_experience.png')
        self.photo = self.photo.subsample(2, 2)
        self.label_photo = None
        self.label = None
        self.imagen = None
        self.Contenedor_Foto = None

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
            try:
                id_entry.insert(0, self.experiencia.Id)
            except AttributeError:
                id_entry.insert(0, "")
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Titulo
        ttk.Label(self.ventana, text="Título: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        titulo_entry = ttk.Entry(self.ventana, textvariable=self.Titulo, font=self.font)
        if self.experiencia is not None:
            try:
                titulo_entry.insert(0, self.experiencia.Titulo)
            except AttributeError:
                titulo_entry.insert(0, self.experiencia.Titulo)
        titulo_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Descripcion
        ttk.Label(self.ventana, text="Descripción: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        descripcion_entry = ttk.Entry(self.ventana, textvariable=self.Descripcion, font=self.font)
        if self.experiencia is not None:
            try:
                descripcion_entry.insert(0, self.experiencia.Descripcion)
            except AttributeError:
                descripcion_entry.insert(0, self.experiencia.Descripcion)
        descripcion_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Fecha celebracion
        ttk.Label(self.ventana, text="Fecha celebración: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        fecha_celebracion_entry = ttk.Entry(self.ventana, textvariable=self.Fecha_Celebracion, font=self.font)
        if self.experiencia is not None:
            try:
                fecha_celebracion_entry.insert(0, self.experiencia.Fecha_Celebracion)
            except AttributeError:
                fecha_celebracion_entry.insert(0, self.experiencia.Fecha_Celebracion)
        fecha_celebracion_entry.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # Precio
        ttk.Label(self.ventana, text="Precio: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        precio_entry = ttk.Entry(self.ventana, textvariable=self.Precio, font=self.font)
        if self.experiencia is not None:
            try:
                precio_entry.insert(0, self.experiencia.Precio)
            except AttributeError:
                precio_entry.insert(0, self.experiencia.Precio)
        precio_entry.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

        # Aforo
        ttk.Label(self.ventana, text="Aforo: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        aforo_entry = ttk.Entry(self.ventana, textvariable=self.Aforo, font=self.font)
        if self.experiencia is not None:
            try:
                aforo_entry.insert(0, self.experiencia.Aforo)
            except AttributeError:
                aforo_entry.insert(0, self.experiencia.Aforo)
        aforo_entry.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la empresa
        ttk.Label(self.ventana, text="Id de la empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        id_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Id_Empresa, font=self.font)
        if self.experiencia is not None:
            try:
                id_empresa_entry.insert(0, self.experiencia.Empresa.Id)
            except AttributeError:
                id_empresa_entry.insert(0, self.experiencia.Empresa.Id)
        id_empresa_entry.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

        # Foto de la experiencia
        ttk.Label(self.ventana, text="Foto de fondo: ", font=self.font).grid(row=16, column=0, sticky="nsew")
        if self.experiencia is not None:
            try:
                img = Image.open(BytesIO(base64.b64decode(self.experiencia.Foto)))
                img = img.resize((50, 50), PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.Contenedor_Foto = tk.Label(self.ventana, image=img)
                self.Contenedor_Foto.image = img
                self.Contenedor_Foto.grid(row=16, column=1, columnspan=2, sticky="nsew")
                self.Foto.set(self.experiencia.Foto)
            except binascii.Error:
                self.Contenedor_Foto = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto.config(width=50, height=50)
                self.Contenedor_Foto.photo = self.photo
                self.Contenedor_Foto.grid(row=16, column=1, columnspan=2, sticky="nsew")
            except PIL.UnidentifiedImageError:
                self.Contenedor_Foto = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto.config(width=50, height=50)
                self.Contenedor_Foto.photo = self.photo
                self.Contenedor_Foto.grid(row=16, column=1, columnspan=2, sticky="nsew")
            except AttributeError:
                self.Contenedor_Foto = tk.Label(self.ventana, image=self.photo)
                self.Contenedor_Foto.config(width=50, height=50)
                self.Contenedor_Foto.photo = self.photo
                self.Contenedor_Foto.grid(row=16, column=1, columnspan=2, sticky="nsew")
        else:
            self.Contenedor_Foto = tk.Label(self.ventana, image=self.photo)
            self.Contenedor_Foto.config(width=50, height=50)
            self.Contenedor_Foto.photo = self.photo
            self.Contenedor_Foto.grid(row=16, column=1, columnspan=2, sticky="nsew")

        ttk.Button(self.ventana, text="Cambiar foto de experiencia", command=lambda: {
            self.obtener_imagen_de_equipo(self.Foto, 16, 1, self.Contenedor_Foto)
        }).grid(row=17, column=1)

        # Botón para actualizar
        if self.experiencia is not None:
            ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=18, column=0, sticky="nsew", padx=5,pady=5, columnspan=2)
        else:
            ttk.Button(self.ventana, text="Insertar", command=self.actualizar_insertar).grid(row=18, column=0, sticky="nsew", padx=5,pady=5, columnspan=2)

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
        from gui.experiencia_gui.manage_experiencias_gui import ExperienciasGui

        nueva_experiencia = None

        if self.experiencia is not None:
            nueva_experiencia = Experiencia(
                Id=self.Id.get(),
                Aforo=self.Aforo.get(),
                Descripcion=self.Descripcion.get(),
                Fecha_Celebracion=self.Fecha_Celebracion.get(),
                empresa=Empresa.empresa_factory_by_id(int(self.Id_Empresa.get())),
                Foto=self.Foto.get(),
                Precio=self.Precio.get(),
                Titulo=self.Titulo.get(),
            )
        else:
            nueva_experiencia = Experiencia(
                Id=-1,
                Aforo=self.Aforo.get(),
                Descripcion=self.Descripcion.get(),
                Fecha_Celebracion=self.Fecha_Celebracion.get(),
                empresa=Empresa.empresa_factory_by_id(int(self.Id_Empresa.get())),
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
