import tkinter as tk
import webservice.web_service_opinion as wso

from tkinter import ttk, messagebox

from model.Opinion import Opinion


class UpdateInsertOpinion:

    def __init__(self, opinion: Opinion):

        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar opinion.")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_preguntando)

        # Datos que necesito
        self.opinion = opinion
        self.Id = tk.StringVar()
        self.Titulo = tk.StringVar()
        self.Descripcion = tk.StringVar()
        self.Fecha = tk.StringVar()
        self.Id_Emoticono = tk.StringVar()
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
            id_entry.insert(0, self.opinion.Id)
        id_entry.config(state="readonly")
        id_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Titulo
        ttk.Label(self.ventana, text="Título: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        titulo_entry = ttk.Entry(self.ventana, textvariable=self.Titulo, font=self.font)
        if self.opinion is not None:
            titulo_entry.insert(0, self.opinion.Titulo)
        titulo_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Descripcion
        ttk.Label(self.ventana, text="Descripción: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        descripcion_entry = ttk.Entry(self.ventana, textvariable=self.Descripcion, font=self.font)
        if self.opinion is not None:
            descripcion_entry.insert(0, self.opinion.Descripcion)
        descripcion_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Fecha
        ttk.Label(self.ventana, text="Fecha: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        fecha_entry = ttk.Entry(self.ventana, textvariable=self.Fecha, font=self.font)
        if self.opinion is not None:
            fecha_entry.insert(0, self.opinion.Fecha)
        fecha_entry.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la emoticon
        ttk.Label(self.ventana, text="Id del emoji: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        id_emoticon_entry = ttk.Entry(self.ventana, textvariable=self.Id_Emoticono, font=self.font)
        if self.opinion is not None:
            id_emoticon_entry.insert(0, self.opinion.Emoticono.Id)
        id_emoticon_entry.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

        # Id del autor
        ttk.Label(self.ventana, text="Id del autor: ", font=self.font).grid(row=5, column=0, sticky="nsew")
        id_autor_entry = ttk.Entry(self.ventana, textvariable=self.Id_Autor, font=self.font)

        if self.opinion is not None:
            id_autor_entry.insert(0, self.opinion.Autor.Id)

        id_autor_entry.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la empresa
        ttk.Label(self.ventana, text="Id de la empresa: ", font=self.font).grid(row=6, column=0, sticky="nsew")
        id_empresa_entry = ttk.Entry(self.ventana, textvariable=self.Id_Empresa, font=self.font)
        try:
            if self.opinion is not None:
                id_empresa_entry.insert(0, self.opinion.Id_Empresa)
        except AttributeError:
            print("No se ha podido cargar la id de la empresa")

        id_empresa_entry.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

        # Id de la experiencia
        ttk.Label(self.ventana, text="Id de la experiencia: ", font=self.font).grid(row=7, column=0, sticky="nsew")
        id_experiencia_entry = ttk.Entry(self.ventana, textvariable=self.Id_Experiencia, font=self.font)

        try:
            if self.opinion is not None:
                id_experiencia_entry.insert(0, self.opinion.Id_Experiencia)
        except AttributeError:
            print("No se ha podido cargar la id de la experiencia")

        id_experiencia_entry.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)

        # Botón para actualizar
        ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_insertar).grid(row=14, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)

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
        from gui.opinion_gui.manage_opiniones_gui import OpinionesGui

        nueva_opinion = Opinion(
            Id=self.Id.get(),
            descripcion=self.Descripcion.get(),
            fecha=self.Fecha.get(),
            # TODO EMOTICONO emoticono=Emoticono(-1, "Emoticono"),
            # TODO AUTOR
            id_empresa=self.Id_Empresa.get(),
            id_experiencia=self.Id_Experiencia.get(),
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
