import binascii
import tkinter as tk

import PIL
import webservice.web_service_persona as wsp
import base64

from io import BytesIO
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from gui.persona_gui.update_insert_personas import UpdateInsertPersona
from model.Persona import Persona


class ExperienciasGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Administrar personas")
        self.ventana.geometry("1280x720")
        self.ventana.resizable(False, False)
        self.center()

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.personas = None

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

    def obtener_personas_actualizadas(self):
        self.personas: list[Persona] = wsp.get_all_personas()
        self.personas.sort(key=lambda x: x.Id)

    def cargar_widgets(self):
        ttk.Button(self.ventana, text="Agregar persona", command=lambda: self.editar_persona(None)).pack(side=tk.TOP,
                                                                                                         fill=tk.X)

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
        self.obtener_personas_actualizadas()
        self.pintar_lista_de_personas()

        # Pinto t.odo en el contenedor
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar.pack(side="right", fill="y")
        self.contenedor.pack(expand=True, fill="both")
        self.canvas.pack(fill="both", expand=True)

        # las scrollbars deben verse en el mismo orden que el contenedor
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

    def pintar_lista_de_personas(self):

        self.lista_foto_perfil = []
        self.lista_foto_fondo = []

        # Muestro el nombre de los campos mostrados
        ttk.Label(self.scrollable_frame, text="Foto Perfil", font=self.font).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Foto Fondo", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Correo", font=self.font).grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Nick", font=self.font).grid(row=0, column=4, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Activo", font=self.font).grid(row=0, column=5, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.personas)):

            # Obtengo la foto de perfil
            try:
                self.base64_string = self.personas[i].Foto_Perfil
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_foto_perfil.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_foto_perfil[i]) \
                    .grid(column=0, row=i + 1, padx=5, pady=5)
            except binascii.Error:
                print("No se pudo cargar la imagen de perfil")
                self.lista_foto_fondo.append(None)
            except PIL.UnidentifiedImageError:
                print("No se pudo cargar la imagen de perfil")
                self.lista_foto_perfil.append(None)
            except AttributeError:
                print("No se pudo cargar la imagen de perfil")
                self.lista_foto_perfil.append(None)

            # Obtengo la foto de fondo
            try:
                self.base64_string = self.personas[i].Foto_Fondo
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_foto_fondo.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_foto_fondo[i]) \
                    .grid(column=1, row=i + 1, padx=5, pady=5)
            except binascii.Error:
                print("No se pudo cargar la imagen de fondo")
                self.lista_foto_fondo.append(None)
            except PIL.UnidentifiedImageError:
                print("No se pudo cargar la imagen de fondo")
                self.lista_foto_fondo.append(None)
            except AttributeError:
                print("No se pudo cargar la imagen de fondo")
                self.lista_foto_fondo.append(None)

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.personas[i].Id, font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
                ttk.Label(self.scrollable_frame, text=self.personas[i].Correo[0:20], font=self.font).grid(row=i + 1, column=3, padx=5, pady=5)
                ttk.Label(self.scrollable_frame, text=self.personas[i].Nick[0:20], font=self.font).grid(row=i + 1, column=4, padx=5, pady=5)
                if self.personas[i].Eliminado:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=5, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=5, padx=5, pady=5)

            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            # Seteo sus botones:
            editar_empresa = ttk.Button(self.scrollable_frame, text="Editar")
            editar_empresa.grid(row=i + 1, column=6, padx=5, pady=5)
            editar_empresa.config(command=lambda iterador=i: {
                self.editar_persona(self.personas[iterador])
            })

            boton_borrar_logicamente = ttk.Button(self.scrollable_frame, text="Activar/Desactivar")
            boton_borrar_logicamente.grid(row=i + 1, column=7, padx=5, pady=5)
            boton_borrar_logicamente.config(command=lambda iterador=i: {
                self.activar_desactivar_persona(iterador)
            })

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=8, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_persona_real(iterador)
            })

    def editar_persona(self, persona):
        self.ventana.destroy()
        UpdateInsertPersona(persona).iniciar_ventana()

    def activar_desactivar_persona(self, iterador):

        if self.personas[iterador].Eliminado == 0:
            if messagebox.askyesno("Desactivar persona", "¿Esta seguro que desea desactivar la persona lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wsp.delete_persona_by_id_logic(self.personas[iterador].Id):
                    messagebox.showinfo("Desactivar persona", "La persona ha sido desactivada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Desactivar persona", "No se pudo desactivar la persona.")
        else:
            if messagebox.askyesno("Activar persona", "¿Esta seguro que desea activar la persona lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wsp.reactivar_persona_by_id_logic(self.personas[iterador].Id):
                    self.actualizar_lista()
                    messagebox.showinfo("Activar persona", "La persona ha sido activada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Activar persona", "No se pudo activar la persona.")

    def eliminar_persona_real(self, iterador):
        if messagebox.askyesno("Eliminar persona", "¿Esta seguro que desea eliminar la persona realmente? Esto afectará en cascada a los elementos que la componen..."):
            if wsp.delete_persona_by_id(self.personas[iterador].Id):
                self.personas.pop(iterador)
                messagebox.showinfo("Eliminar persona", "La persona ha sido eliminada correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar persona", "No se pudo eliminar la persona.")

    def actualizar_lista(self):
        self.obtener_personas_actualizadas()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_personas()

    def iniciar_ventana(self):
        self.ventana.mainloop()
