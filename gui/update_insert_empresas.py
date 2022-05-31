import tkinter as tk

from tkinter import ttk

from model.Empresa import Empresa


class UpdateInsertEmpresa:

    def __init__(self, empresa: Empresa):
        # La ventana en si
        self.ventana = tk.Tk()
        self.ventana.title("Actualizar/Insertar empresa.")

        # Datos que necesito
        self.empresa = empresa

        # Fuente
        self.font = ("Montserrat Light", 12)

        # inicializo esos elementos
        self.cargar_widgets()

    def cargar_widgets(self):
        # Id de la empresa
        ttk.Label(self.ventana, text="Id: ", font=self.font).grid(row=0, column=0, sticky="nsew")
        ttk.Entry(self.ventana, textvariable=self.empresa.Id, font=self.font).grid(row=0, column=1)

        # Correo de la empresa
        ttk.Label(self.ventana, text="Correo: ", font=self.font).grid(row=1, column=0, sticky="nsew")
        ttk.Entry(self.ventana, textvariable=self.empresa.Correo, font=self.font).grid(row=1, column=1)

        # Contraseña de la empresa
        ttk.Label(self.ventana, text="Contraseña: ", font=self.font).grid(row=2, column=0, sticky="nsew")
        ttk.Entry(self.ventana, textvariable=self.empresa.Contrasena, font=self.font).grid(row=2, column=1)

        # Nick de la empresa
        ttk.Label(self.ventana, text="Nick: ", font=self.font).grid(row=3, column=0, sticky="nsew")
        ttk.Entry(self.ventana, textvariable=self.empresa.Nick, font=self.font).grid(row=3, column=1)

        # Frase de la empresa
        ttk.Label(self.ventana, text="Frase: ", font=self.font).grid(row=4, column=0, sticky="nsew")
        ttk.Entry(self.ventana, textvariable=self.empresa.Frase, font=self.font).grid(row=4, column=1)

        # Nombre de la empresa
        ttk.Label(self.ventana, text="Nombre: ", font=self.font).grid(row=5, column=0, sticky="nsew")

    def iniciar_ventana(self):
        self.ventana.mainloop()