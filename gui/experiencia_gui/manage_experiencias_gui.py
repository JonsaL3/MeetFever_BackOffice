import binascii
import tkinter as tk
from pathlib import Path

import PIL
import webservice.web_service_experiencia as wse
import base64

from io import BytesIO
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from model.Experiencia import Experiencia
from gui.experiencia_gui.update_insert_experiencias import UpdateInsertExperiencias

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../assets")


def relative_to_assets(path: str) -> Path:
    print(ASSETS_PATH / Path(path))
    return ASSETS_PATH / Path(path)


class ExperienciasGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.iconbitmap(relative_to_assets("indytek_logo.ico"))
        self.ventana.title("Administrar experiencias")
        self.ventana.geometry("1370x720")
        self.center()
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_menu)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.experiencias = None

        # Foto por defecto
        self.photo = tk.PhotoImage(file='assets/default_experience.png')
        self.photo = self.photo.subsample(2, 2)
        self.label_photo = None

        # Elementos internos que en cualquier lenguaje normal serían prescindibles
        self.lista_fotos_experiencia = None
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

    def obtener_experiencias_actualizadas(self):
        self.experiencias: list[Experiencia] = wse.get_all_experiencias()
        self.experiencias.sort(key=lambda x: x.Id)

    def cargar_widgets(self):
        ttk.Button(self.ventana, text="Agregar experiencia", command=lambda: self.editar_persona(None)).pack(side=tk.TOP, fill=tk.X)

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
        self.obtener_experiencias_actualizadas()
        self.pintar_lista_de_personas()

        # Pinto t.odo en el contenedor
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar.pack(side="right", fill="y")
        self.contenedor.pack(expand=True, fill="both")
        self.canvas.pack(fill="both", expand=True)

        # las scrollbars deben verse en el mismo orden que el contenedor
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

        self.mostrar_mensaje_si_hay_desactivaciones_pendientes()

    def cargar_foto_por_defecto(self, row, column, pos, lista):
        lista.append(None)
        self.label_photo = tk.Label(row, image=self.photo)
        self.label_photo.config(width=50, height=50)
        self.label_photo.photo = self.photo
        self.label_photo.grid(column=column, row=pos + 1, padx=5, pady=5)

    def mostrar_mensaje_si_hay_desactivaciones_pendientes(self):
        for experiencia in self.experiencias:
            if experiencia.Borrado_Solicitado:
                messagebox.showinfo("Aviso", "Hay experiencias con solicitud de borrado. Confirmelas si lo considera.")
                return

    def pintar_lista_de_personas(self):

        self.lista_fotos_experiencia = []

        # Muestro el nombre de los campos mostrados
        ttk.Label(self.scrollable_frame, text="Imagen experiencia", font=self.font).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Titulo", font=self.font).grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Descripción", font=self.font).grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Fecha", font=self.font).grid(row=0, column=4, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Precio", font=self.font).grid(row=0, column=5, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Aforo", font=self.font).grid(row=0, column=6, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Activo", font=self.font).grid(row=0, column=7, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.experiencias)):

            # Obtengo la foto de la experiencia
            try:
                self.base64_string = self.experiencias[i].Foto
                self.image = Image.open(BytesIO(base64.b64decode(self.base64_string)))
                self.image = self.image.resize((50, 50), PIL.Image.ANTIALIAS)
                self.lista_fotos_experiencia.append(ImageTk.PhotoImage(self.image))
                ttk.Label(self.scrollable_frame, image=self.lista_fotos_experiencia[i]).grid(column=0, row=i + 1, padx=5, pady=5, )
            except binascii.Error:
                self.cargar_foto_por_defecto(self.scrollable_frame, 0, i, self.lista_fotos_experiencia)
            except PIL.UnidentifiedImageError:
                self.cargar_foto_por_defecto(self.scrollable_frame, 0, i, self.lista_fotos_experiencia)
            except AttributeError:
                self.cargar_foto_por_defecto(self.scrollable_frame, 0, i, self.lista_fotos_experiencia)

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Id, font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Titulo[0:20], font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Descripcion[0:20], font=self.font).grid(row=i + 1, column=3, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Fecha_Celebracion, font=self.font).grid(row=i + 1, column=4, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Precio, font=self.font).grid(row=i + 1,column=5,padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                ttk.Label(self.scrollable_frame, text=self.experiencias[i].Aforo, font=self.font).grid(row=i + 1,column=6, padx=5,pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            try:
                if self.experiencias[i].Eliminado:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=7, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=7, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            # Seteo sus botones:
            editar_empresa = ttk.Button(self.scrollable_frame, text="Editar")
            editar_empresa.grid(row=i + 1, column=8, padx=5, pady=5)
            editar_empresa.config(command=lambda iterador=i: {
                self.editar_persona(self.experiencias[iterador])
            })

            boton_borrar_logicamente = ttk.Button(self.scrollable_frame, text="Activar/Desactivar")
            boton_borrar_logicamente.grid(row=i + 1, column=9, padx=5, pady=5)
            boton_borrar_logicamente.config(command=lambda iterador=i: {
                self.activar_desactivar_persona(iterador)
            })

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=10, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_persona_real(iterador)
            })

            if self.experiencias[i].Borrado_Solicitado:
                boton_confirmar_borrado_logico = ttk.Button(self.scrollable_frame, text="Confirmar")
                boton_confirmar_borrado_logico.config(command=lambda iterador=i: {
                    self.confirmar_borrado_logico(iterador)
                })
                boton_confirmar_borrado_logico.grid(row=i + 1, column=11, padx=5, pady=5)

    def editar_persona(self, persona):
        self.ventana.destroy()
        UpdateInsertExperiencias(persona).iniciar_ventana()

    def confirmar_borrado_logico(self, iterador):
        wse.confirmar_solicitud_borrado(self.experiencias[iterador].Id)
        wse.delete_experiencia_by_id_logic(self.experiencias[iterador].Id)
        self.actualizar_lista()

    def activar_desactivar_persona(self, iterador):

        if self.experiencias[iterador].Eliminado == 0:
            if messagebox.askyesno("Desactivar experiencia", "¿Esta seguro que desea desactivar la experiencia lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wse.delete_experiencia_by_id_logic(self.experiencias[iterador].Id):
                    messagebox.showinfo("Desactivar experiencia", "La experiencia ha sido desactivada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Desactivar experiencia", "No se pudo desactivar la experiencia.")
        else:
            if messagebox.askyesno("Activar experiencia", "¿Esta seguro que desea activar la experiencia lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wse.reactivar_experiencia_by_id(self.experiencias[iterador].Id):
                    self.actualizar_lista()
                    messagebox.showinfo("Activar experiencia", "La experiencia ha sido activada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Activar experiencia", "No se pudo activar la experiencia.")

    def eliminar_persona_real(self, iterador):
        if messagebox.askyesno("Eliminar experiencia", "¿Esta seguro que desea eliminar la experiencia realmente? Esto afectará en cascada a los elementos que la componen..."):
            if wse.delete_experiencia_by_id(self.experiencias[iterador].Id):
                self.experiencias.pop(iterador)
                messagebox.showinfo("Eliminar experiencia", "La experiencia ha sido eliminada correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar experiencia", "No se pudo eliminar la experiencia.")

    def actualizar_lista(self):
        self.obtener_experiencias_actualizadas()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_personas()

    def iniciar_ventana(self):
        self.ventana.mainloop()
