import tkinter as tk
import webservice.web_service_sexo as wss

from model.Sexo import Sexo
from tkinter import ttk, messagebox
from gui.sexo_gui.update_insert_sexos import UpdateInsertSexo


class SexosGui:

    def __init__(self):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Administrar sexos")
        self.ventana.geometry("520x720")
        self.center()
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_menu)

        # Fuente
        self.font = ("Montserrat Light", 12)

        # Lista de empresas
        self.sexos = None

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

    def obtener_sexos_actualizados(self):
        self.sexos: list[Sexo] = wss.get_all_sexos()
        self.sexos.sort(key=lambda x: x.Id)

    def cargar_widgets(self):
        ttk.Button(self.ventana, text="Agregar sexos", command=lambda: self.editar_sexo(None)).pack(side=tk.TOP, fill=tk.X)

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
        self.obtener_sexos_actualizados()
        self.pintar_lista_de_sexos()

        # Pinto t.odo en el contenedor
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar.pack(side="right", fill="y")
        self.contenedor.pack(expand=True, fill="both")
        self.canvas.pack(fill="both", expand=True)

        # las scrollbars deben verse en el mismo orden que el contenedor
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

    def pintar_lista_de_sexos(self):
        # Muestro el nombre de los campos mostrados
        ttk.Label(self.scrollable_frame, text="Id", font=self.font).grid(row=0, column=0, padx=5,pady=5)
        ttk.Label(self.scrollable_frame, text="Sexo", font=self.font).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.scrollable_frame, text="Activo", font=self.font).grid(row=0, column=2, padx=5, pady=5)

        # Pinto las empresas junto a sus opciones en el scroll
        for i in range(len(self.sexos)):

            # pinto el resto de sus atributos
            try:
                ttk.Label(self.scrollable_frame, text=self.sexos[i].Id, font=self.font).grid(row=i + 1, column=0, padx=5, pady=5)
                ttk.Label(self.scrollable_frame, text=self.sexos[i].Sexo[0:20], font=self.font).grid(row=i + 1, column=1, padx=5, pady=5)
                if self.sexos[i].Eliminado:
                    ttk.Label(self.scrollable_frame, text="No", font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
                else:
                    ttk.Label(self.scrollable_frame, text="Si", font=self.font).grid(row=i + 1, column=2, padx=5, pady=5)
            except AttributeError:
                print("No se pudo cargar el resto de los atributos")

            # Seteo sus botones:
            editar_empresa = ttk.Button(self.scrollable_frame, text="Editar")
            editar_empresa.grid(row=i + 1, column=3, padx=5, pady=5)
            editar_empresa.config(command=lambda iterador=i: {
                self.editar_sexo(self.sexos[iterador])
            })

            boton_borrar_logicamente = ttk.Button(self.scrollable_frame, text="Activar/Desactivar")
            boton_borrar_logicamente.grid(row=i + 1, column=4, padx=5, pady=5)
            boton_borrar_logicamente.config(command=lambda iterador=i: {
                self.activar_desactivar_sexo(iterador)
            })

            boton_borrar = ttk.Button(self.scrollable_frame, text="Eliminar")
            boton_borrar.grid(row=i + 1, column=10, padx=5, pady=5)
            boton_borrar.config(command=lambda iterador=i: {
                self.eliminar_persona_real(iterador)
            })

    def editar_sexo(self, sexo):
        self.ventana.destroy()
        UpdateInsertSexo(sexo).iniciar_ventana()

    def activar_desactivar_sexo(self, iterador):

        if self.sexos[iterador].Eliminado == 0:
            if messagebox.askyesno("Desactivar sexo", "¿Esta seguro que desea desactivar el sexo lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wss.delete_sexo_by_id_logico(self.sexos[iterador].Id):
                    messagebox.showinfo("Desactivar sexo", "El sexo ha sido desactivada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Desactivar sexo", "No se pudo desactivar el sexo.")
        else:
            if messagebox.askyesno("Activar sexo", "¿Esta seguro que desea activar el sexo lógicamente? Esto afectará en cascada a los elementos que la componen..."):
                if wss.reactivar_sexo_by_id_logico(self.sexos[iterador].Id):
                    self.actualizar_lista()
                    messagebox.showinfo("Activar sexo", "El sexo ha sido activada correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Activar sexo", "No se pudo activar el sexo.")

    def eliminar_persona_real(self, iterador):
        if messagebox.askyesno("Eliminar sexo", "¿Esta seguro que desea eliminar el sexo realmente? Esto afectará en cascada a los elementos que la componen..."):
            if wss.delete_sexo_by_id(self.sexos[iterador].Id):
                self.sexos.pop(iterador)
                messagebox.showinfo("Eliminar sexo", "El sexo ha sido eliminada correctamente.")
                self.actualizar_lista()
            else:
                messagebox.showerror("Eliminar sexo", "No se pudo eliminar el sexo.")

    def actualizar_lista(self):
        self.obtener_sexos_actualizados()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.pintar_lista_de_sexos()

    def iniciar_ventana(self):
        self.ventana.mainloop()
