import binascii
import tkinter as tk

import PIL
import webservice.web_service_empresa as wse
import base64

from io import BytesIO
from tkinter import ttk, simpledialog, messagebox
from model.Empresa import Empresa
from PIL import Image, ImageTk


class EmpresasGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Administrar empresas")
        self.ventana.geometry("1280x720")
        self.ventana.configure(bg="#F4F4F4")
        self.ventana.resizable(False, False)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.empresas = None

        # Elementos internos que en cualquier lenguaje normal serían prescindibles
        self.lista_foto_perfil = None
        self.lista_foto_fondo = None
        self.base64_string = None
        self.image = None

        # Elementos que la componen
        self.contenedor = None
        self.scrollable_frame = None
        self.xscrollbar = None
        self.yscrollbar = None
        self.canvas = None

        # inicializo esos elementos
        self.cargar_widgets()

    def obtener_empresas_actualizadas(self):
        self.empresas: list[Empresa] = wse.get_all_empresas()
        self.empresas.sort(key=lambda x: x.Id)

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
        self.obtener_empresas_actualizadas()
        self.pintar_lista_de_empresas()

        # Pinto t.odo en el contenedor
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar.pack(side="right", fill="y")
        self.contenedor.pack(expand=True, fill="both")
        self.canvas.pack(fill="both", expand=True)

        # las scrollbars deben verse en el mismo orden que el contenedor
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

    def pintar_lista_de_empresas(self):

        self.lista_foto_perfil = []
        self.lista_foto_fondo = []

        # Muestro el nombre de los campos mostrados
        ttk.Label(self.scrollable_frame, text="Foto Perfil", font=self.font).grid(row=0, column=0)
        ttk.Label(self.scrollable_frame, text="Foto Fondo", font=self.font).grid(row=0, column=1)
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=2, padx=10, pady=10)
        ttk.Label(self.scrollable_frame, text="Correo", font=self.font).grid(row=0, column=3, padx=10, pady=10)
        ttk.Label(self.scrollable_frame, text="Nick", font=self.font).grid(row=0, column=4, padx=10, pady=10)
        ttk.Label(self.scrollable_frame, text="Nombre Empresa", font=self.font).grid(row=0, column=5, padx=10, pady=10)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.empresas)):

            # Obtengo la foto de perfil
            try:
                self.base64_string = self.empresas[i].Foto_Perfil
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_foto_perfil.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_foto_perfil[i]) \
                    .grid(column=0, row=i + 1, padx=10, pady=10)
            except binascii.Error:
                print("No se pudo cargar la imagen de perfil")

            # Obtengo la foto de fondo
            try:
                self.base64_string = self.empresas[i].Foto_Fondo
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_foto_fondo.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_foto_fondo[i]) \
                    .grid(column=1, row=i + 1, padx=10, pady=10)
            except binascii.Error:
                print("No se pudo cargar la imagen de fondo")

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.empresas[i].Id, font=self.font).grid(row=i + 1, column=2, padx=10,
                                                                                      pady=10)
                ttk.Label(self.scrollable_frame, text=self.empresas[i].Correo, font=self.font).grid(row=i + 1, column=3, padx=10,
                                                                                          pady=10)
                ttk.Label(self.scrollable_frame, text=self.empresas[i].Nick, font=self.font).grid(row=i + 1, column=4, padx=10,
                                                                                        pady=10)
                ttk.Label(self.scrollable_frame, text=self.empresas[i].Nombre_Empresa, font=self.font).grid(row=i + 1, column=5,
                                                                                                  padx=10, pady=10)
            except AttributeError:
                ttk.Label(self.scrollable_frame, text="").grid(row=i + 1, column=5, padx=10, pady=10)

            # Seteo sus botones:
            ttk.Button(self.scrollable_frame, text="Editar").grid(row=i + 1, column=6, padx=10, pady=10)

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=7, padx=10, pady=10)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_empresa(iterador)
            })

    def eliminar_empresa(self, iterador):
        if messagebox.askyesno("Eliminar empresa", "¿Esta seguro que desea eliminar la empresa lógicamente? Esto afectará en cascada a los elementos que la componen..."):
            # wse.delete_empresa_by_id_logic(self.empresas[iterador].Id)
            self.empresas.pop(iterador)
            messagebox.showinfo("Eliminar empresa", "La empresa ha sido eliminada correctamente.")
            self.actualizar_lista()

    def actualizar_lista(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        # self.obtener_empresas_actualizadas()
        self.pintar_lista_de_empresas()

    def cerrar_ventana(self):
        self.ventana.destroy()

    def iniciar_ventana(self):
        self.ventana.mainloop()
