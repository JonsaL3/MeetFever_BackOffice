import base64
import binascii
import tkinter as tk
from io import BytesIO

import PIL
from PIL import Image, ImageTk

import webservice.web_service_opinion as wso
import webservice.web_service_emoticono as wse

from tkinter import ttk, messagebox

from model.Emoticono import Emoticono
from model.Opinion import Opinion

icono_seleccionado = None


def pintar_lista_emoticonos():
    ventana_emoji = tk.Toplevel()
    ventana_emoji.title("Lista de Emoticonos")
    ventana_emoji.resizable(False, False)
    ventana_emoji.update_idletasks()

    emoticonos = wse.get_all_emoticonos()

    for i in range(len(emoticonos)):

        img = Image.open(BytesIO(base64.b64decode(emoticonos[i].Emoji)))
        img = img.resize((50, 50), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        def set_icono_seleccionado(emoticono: Emoticono):
            global icono_seleccionado
            icono_seleccionado = emoticono
            ventana_emoji.destroy()

        # creo un boton con esa imagen
        boton = ttk.Button(ventana_emoji, image=img)
        boton.image = img
        boton.config(command=lambda: set_icono_seleccionado(emoticonos[i]))
        boton.grid(row=i, column=0, padx=10, pady=10)

        ttk.Label(ventana_emoji, text="Emoticono " + str(emoticonos[i].Id)).grid(row=i, column=1, padx=10, pady=10)

    ventana_emoji.mainloop()


class UpdateInsertOpinion:

    def __init__(self, opinion: Opinion):

        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar opinion.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)
        self.ventana.resizable(False, False)

        # Datos que necesito
        self.opinion = opinion
        self.Id = tk.StringVar()
        self.Titulo = tk.StringVar()
        self.Descripcion = tk.StringVar()
        self.Fecha = tk.StringVar()
        self.Id_Autor = tk.StringVar()
        self.Id_Empresa = tk.StringVar()
        self.Id_Experiencia = tk.StringVar()

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cerrar_ventana_preguntando(self):
        if messagebox.askokcancel("Cerrar", "¿Está seguro que desea cerrar la ventana? Esto descartará los cambios."):
            from gui.opinion_gui.manage_opiniones_gui import OpinionesGui
            self.ventana.destroy()
            OpinionesGui().iniciar_ventana()

    def cargar_widgets(self):
        # Id de la empresa
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        id_entry = ttk.Entry(self.ventana, textvariable=self.Id, font=self.font)
        if self.opinion is not None:
            try:
                id_entry.insert(0, self.opinion.Id)
            except AttributeError:
                id_entry.insert(0, "")
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Titulo
        ttk.Label(self.ventana, text="Título: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        titulo_entry = ttk.Entry(self.ventana, textvariable=self.Titulo, font=self.font)
        if self.opinion is not None:
            try:
                titulo_entry.insert(0, self.opinion.Titulo)
            except AttributeError:
                titulo_entry.insert(0, "")
        titulo_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Descripcion
        ttk.Label(self.ventana, text="Descripción: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        descripcion_entry = ttk.Entry(self.ventana, textvariable=self.Descripcion, font=self.font)
        if self.opinion is not None:
            try:
                descripcion_entry.insert(0, self.opinion.Descripcion)
            except AttributeError:
                descripcion_entry.insert(0, "")
        descripcion_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Fecha
        ttk.Label(self.ventana, text="Fecha: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        fecha_entry = ttk.Entry(self.ventana, textvariable=self.Fecha, font=self.font)
        if self.opinion is not None:
            try:
                fecha_entry.insert(0, self.opinion.Fecha)
            except AttributeError:
                fecha_entry.insert(0, "")
        fecha_entry.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # Id del autor
        ttk.Label(self.ventana, text="Id del autor: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        id_autor_entry = ttk.Entry(self.ventana, textvariable=self.Id_Autor, font=self.font)
        if self.opinion is not None:
            try:
                id_autor_entry.insert(0, self.opinion.Autor.Id)
            except AttributeError:
                id_autor_entry.insert(0, "")
        id_autor_entry.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la empresa
        ttk.Label(self.ventana, text="Id de la empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        id_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Id_Empresa, font=self.font)
        try:
            if self.opinion is not None:
                try:
                    id_empresa_entry.insert(0, self.opinion.Id_Empresa)
                except AttributeError:
                    id_empresa_entry.insert(0, "")
        except AttributeError:
            print("No se ha podido cargar la id de la empresa")

        id_empresa_entry.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la experiencia
        ttk.Label(self.ventana, text="Id de la experiencia: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        id_experiencia_entry = ttk.Entry(self.ventana, textvariable=self.Id_Experiencia, font=self.font)
        try:
            if self.opinion is not None:
                try:
                    id_experiencia_entry.insert(0, self.opinion.Id_Experiencia)
                except AttributeError:
                    id_experiencia_entry.insert(0, "")
        except AttributeError:
            print("No se ha podido cargar la id de la experiencia")
        id_experiencia_entry.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)

        boton_seleccionar_emoticono = ttk.Button(self.ventana, text="Seleccionar Emoticono",
                                                 command=lambda: pintar_lista_emoticonos())
        boton_seleccionar_emoticono.grid(row=8, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Botón para actualizar
        if self.opinion is not None:
            ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=9, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)
        else:
            ttk.Button(self.ventana, text="Insertar", command=self.actualizar_insertar).grid(row=9, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)

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

        global icono_seleccionado

        # Lo importo aqui para evitar circular imports
        from gui.opinion_gui.manage_opiniones_gui import OpinionesGui

        nueva_opinion = None
        id_autor_definitivo = None
        id_empresa_definitivo = None
        id_experiencia_definitivo = None

        if self.Id_Autor.get() != "":
            id_autor_definitivo = self.Id_Autor.get()

        if self.Id_Empresa.get() != "":
            id_empresa_definitivo = self.Id_Empresa.get()

        if self.Id_Experiencia.get() != "":
            id_experiencia_definitivo = self.Id_Experiencia.get()

        if self.opinion is not None:

            print("ICONO SELECCIONADO", icono_seleccionado.Id)

            # TODO NO TERMINA DE PILLAR EL EMOJI QUE HE SELECCIONADO AL MODIFICAR LA OPINION

            if icono_seleccionado is None:
                icono_seleccionado = self.opinion.Emoticono

            nueva_opinion = Opinion(
                Id=self.Id.get(),
                descripcion=self.Descripcion.get(),
                fecha=self.Fecha.get(),
                emoticono=icono_seleccionado,
                id_autor=id_autor_definitivo,
                id_empresa=id_empresa_definitivo,
                id_experiencia=id_experiencia_definitivo,
                titulo=self.Titulo.get(),
                like=False,
                numero_likes=0
            )

        if self.opinion is None:
            if wso.insert_opinion(nueva_opinion):
                messagebox.showinfo("Insertado", "Opinión insertada correctamente.")
                self.ventana.destroy()
                OpinionesGui().iniciar_ventana()
        else:
            if wso.update_opinion(nueva_opinion):
                messagebox.showinfo("Actualizado", "Persona Opinión correctamente.")
                self.ventana.destroy()
                OpinionesGui().iniciar_ventana()

    def iniciar_ventana(self):
        self.ventana.mainloop()
