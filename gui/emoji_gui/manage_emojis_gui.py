import base64
import binascii
import tkinter as tk
from io import BytesIO
from tkinter import ttk, messagebox

import PIL
from PIL import Image, ImageTk

import webservice.web_service_emoticono as wse
from gui.emoji_gui.update_insert_emoji import UpdateInsertEmoji
from model.Emoticono import Emoticono


class EmojisGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Administrar emoticonos")
        self.ventana.geometry("510x720")
        self.center()
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_menu)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.emoticonos = None

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

    def volver_a_menu(self):
        from gui.main_gui import MainGui
        self.ventana.destroy()
        MainGui().iniciar_ventana()

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

    def obtener_emoticonos_actualizados(self):
        self.emoticonos: list[Emoticono] = wse.get_all_emoticonos()
        self.emoticonos.sort(key=lambda x: x.Id)

    def cargar_widgets(self):
        ttk.Button(self.ventana, text="Agregar emoji", command=lambda: self.editar_emoji(None)).pack(side=tk.TOP, fill=tk.X)

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
        self.obtener_emoticonos_actualizados()
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
        ttk.Label(self.scrollable_frame, text="Emoticono", font=self.font).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Activo", font=self.font).grid(row=0, column=2, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.emoticonos)):

            # Pinto el propio emoticono:
            try:
                self.base64_string = self.emoticonos[i].Emoji
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_foto_fondo.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_foto_fondo[i]) \
                    .grid(column=0, row=i + 1, padx=5, pady=5)
            except binascii.Error:
                print("No se pudo cargar la imagen de fondo")
                self.lista_foto_fondo.append(None)
            except PIL.UnidentifiedImageError:
                print("No se pudo cargar la imagen de fondo")
                self.lista_foto_fondo.append(None)

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.emoticonos[i].Id, font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
                if self.emoticonos[i].Eliminado:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)

            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            # Seteo sus botones:
            editar_empresa = ttk.Button(self.scrollable_frame, text="Editar")
            editar_empresa.grid(row=i + 1, column=6, padx=5, pady=5)
            editar_empresa.config(command=lambda iterador=i: {
                self.editar_emoji(self.emoticonos[iterador])
            })

            boton_borrar_logicamente = ttk.Button(self.scrollable_frame, text="Activar/Desactivar")
            boton_borrar_logicamente.grid(row=i + 1, column=7, padx=5, pady=5)
            boton_borrar_logicamente.config(command=lambda iterador=i: {
                self.activar_desactivar_emoji(iterador)
            })

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=8, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_emoticono_real(iterador)
            })

    def editar_emoji(self, emoji):
        self.ventana.destroy()
        UpdateInsertEmoji(emoji).iniciar_ventana()

    def activar_desactivar_emoji(self, iterador):

        if self.emoticonos[iterador].Eliminado == 0:
            if messagebox.askyesno("Desactivar emoticono", "¿Esta seguro que desea desactivar el emoticono lógicamente? Esto afectará en cascada a los elementos que le componen..."):
                if wse.delete_emoticono_by_id_logic(self.emoticonos[iterador].Id):
                    messagebox.showinfo("Desactivar emoticono", "El emoticono ha sido desactivado correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Desactivar emoticono", "No se pudo desactivar el emoticono.")
        else:
            if messagebox.askyesno("Activar emoticono", "¿Esta seguro que desea activar el emoticono lógicamente? Esto afectará en cascada a los elementos que le componen..."):
                if wse.reactivar_emoticono_by_id_logic(self.emoticonos[iterador].Id):
                    self.actualizar_lista()
                    messagebox.showinfo("Activar emoticono", "El emoticono ha sido activado correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Activar emoticono", "No se pudo activar el emoticono.")

    def eliminar_emoticono_real(self, iterador):
        if messagebox.askyesno("Eliminar emoticono", "¿Esta seguro que desea eliminar el emoticono realmente? Esto afectará en cascada a los elementos que la componen..."):
            if wse.eliminar_emoticono(self.emoticonos[iterador].Id):
                self.emoticonos.pop(iterador)
                messagebox.showinfo("Eliminar emoticono", "El emoticono ha sido eliminado correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar emoticono", "No se pudo eliminar el emoticono.")

    def actualizar_lista(self):
        self.obtener_emoticonos_actualizados()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_personas()

    def iniciar_ventana(self):
        self.ventana.mainloop()
