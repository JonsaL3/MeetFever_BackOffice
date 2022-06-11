import base64
import binascii
import tkinter as tk
from io import BytesIO

import PIL
from PIL import ImageTk, Image

import webservice.web_service_opinion as wso

from tkinter import ttk, messagebox
from gui.opinion_gui.update_insert_opiniones import UpdateInsertOpinion
from model.Opinion import Opinion


class OpinionesGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Administrar opiniones")
        self.ventana.geometry("960x720")
        self.center()
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_menu)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.opiniones = None

        # Elementos que la componen
        self.contenedor = None
        self.scrollable_frame = None
        self.xscrollbar = None
        self.yscrollbar = None
        self.canvas = None

        self.image = None
        self.base64_string = None

        self.lista_emojis = []

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

    def obtener_personas_actualizadas(self):
        self.opiniones: list[Opinion] = wso.get_all_opiniones()
        self.opiniones.sort(key=lambda x: x.Id)

    def cargar_widgets(self):
        ttk.Button(self.ventana, text="Agregar opinion", command=lambda: self.editar_persona(None)).pack(side=tk.TOP, fill=tk.X)

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

        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Contenido", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Fecha", font=self.font).grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Activo", font=self.font).grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Emoticono", font=self.font).grid(row=0, column=4, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.opiniones)):

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.opiniones[i].Id, font=self.font).grid(row=i + 1, column=0, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.opiniones[i].Descripcion[0:20], font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
            except:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.opiniones[i].Fecha, font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
            except:
                print("No se pudo cargar el resto de los atributos")

            try:
                if self.opiniones[i].Eliminado == 0:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=3, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=3, padx=5, pady=5)
            except:
                print("No se pudo cargar el resto de los atributos")

            try:
                self.base64_string = self.opiniones[i].Emoticono.Emoji
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_emojis.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_emojis[i]).grid(column=4, row=i + 1, padx=5, pady=5)
            except binascii.Error:
                print("No se puede cargar el emoji")
            except PIL.UnidentifiedImageError:
                print("No se puede cargar el emoji")
            except AttributeError:
                print("No se puede cargar el emoji")

            # Seteo sus botones:
            editar_empresa = ttk.Button(self.scrollable_frame, text="Editar")
            editar_empresa.grid(row=i + 1, column=5, padx=5, pady=5)
            editar_empresa.config(command=lambda iterador=i: {
                self.editar_persona(self.opiniones[iterador])
            })

            boton_borrar_logicamente = ttk.Button(self.scrollable_frame, text="Activar/Desactivar")
            boton_borrar_logicamente.grid(row=i + 1, column=6, padx=5, pady=5)
            boton_borrar_logicamente.config(command=lambda iterador=i: {
                self.activar_desactivar_empresa(iterador)
            })

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=7, padx=5, pady=5)
            boton_borrar.grid(row=i + 1, column=7, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_empresa_real(iterador)
            })

    def editar_persona(self, persona):
        self.ventana.destroy()
        UpdateInsertOpinion(persona).iniciar_ventana()

    def activar_desactivar_empresa(self, iterador):
        if self.opiniones[iterador].Eliminado == 0:
            if messagebox.askyesno("Desactivar opinion", "¿Esta seguro que desea desactivar la opinión lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wso.delete_opinion_by_id_logic(self.opiniones[iterador].Id):
                    messagebox.showinfo("Desactivar opinión", "La opinión ha sido eliminada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Desactivar opinión", "La opinión no pudo ser eliminada.")
        else:
             if messagebox.askyesno("Reactivar opinion", "¿Esta seguro que desea reactivar la opinión lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wso.reactivar_opinion_by_id_logic(self.opiniones[iterador].Id):
                    messagebox.showinfo("Reactivar opinión", "La opinión ha sido reactivada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Error", "No se pudo reactivar la opinión.")

    def eliminar_empresa_real(self, iterador):
        if messagebox.askyesno("Eliminar opinion", "¿Esta seguro que desea eliminar la opinión realmente? Esto afectará en cascada a los elementos que la componen..."):
            if wso.delete_opinion_by_id(self.opiniones[iterador].Id):
                self.opiniones.pop(iterador)
                messagebox.showinfo("Eliminar opinión", "La opinión ha sido eliminada correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar opinión", "La opinión no se pudo eliminar.")

    def actualizar_lista(self):
        self.obtener_personas_actualizadas()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_personas()

    def iniciar_ventana(self):
        self.ventana.mainloop()
