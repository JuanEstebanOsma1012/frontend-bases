import customtkinter as ctk
from export.export import create_report as cr

class MainGUI:

    exportation_types = {
        1: "pdf",
        2: "svg",
        3: "png",
        4: "jpg"
    }

    reports = {
        1: {
            "name": "Distribucion de cursos por horario",
            "pseudoname": "report1",
            "description": "Este reporte muestra una grafica de pastel que muestra la cantidad de cursos que hay en un horario en particular"
        },
        2: {
            "name": "Distribucion de preguntas por tipo",
            "pseudoname": "report2",
            "description": "Este grafico muestra la cantidad de preguntas que hay almacenadas en el sistema de cada tipo (seleccion multiple o abierta)"
        },
        3: {
            "name": "Heatmap de Quices por tema y profesor",
            "pseudoname": "report3",
            "description": "Este reporte muestra un grafico de calor que distribuye la cantidad de quices que hay de cada profesor en cada materia en particular"
        },
        4: {
            "name": "Heatmap de calificacion por tema y grupo",
            "pseudoname": "report4",
            "description": "Este reporte muestra un grafico de calor que distribuye la calificacion promedio de quices que hay de cada grupo en cada tema que se ve"
        },
        5: {
            "name": "Desempeño estudiantil a lo largo del tiempo",
            "pseudoname": "report5",
            "description": "Este reporte muestra el desempeño promedio estudiantil en cada mes"
        },
        6: {
            "name": "Cantidad de quices a lo largo del tiempo",
            "pseudoname": "report6",
            "description": "Este reporte muestra una linea de tiempo de la cantidad de quices que se han registrado basado en su fecha de finalizacion"
        },
        7: {
            "name": "Cantidad de bancos por profesor y cantidad de preguntas promedio por banco",
            "pseudoname": "report7",
            "description": "Este reporte muestra la cantidad de bancos que tiene cada profesor y la cantidad de preguntas promedio que tiene cada banco"
        }
    }

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        root = ctk.CTk()
        root.geometry("800x600")

        report_description = ctk.StringVar()

        report_num = ctk.IntVar()
        report_num.trace("w", lambda name, index, mode, report_num=report_num: report_description.set(self.reports[report_num.get()]["description"]))
        report_num.set(1)

        exportation = ctk.IntVar()
        exportation.set(1)

        def callback():
            cr(self.reports[report_num.get()]["pseudoname"], self.exportation_types[exportation.get()])

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=10, padx=10, fill="both", expand=True)

        title = ctk.CTkLabel(master=frame, text="Bienvenido al generador de reportes", font=("Arial", 30))
        title.pack(pady=7, padx=10)

        subtitle = ctk.CTkLabel(master=frame, text="Por favor seleccione el reporte que desea generar y el tipo de exportacion:", font=("Arial", 20))
        subtitle.pack(pady=7, padx=10, anchor=ctk.W)

        options = ctk.CTkFrame(master=frame)
        options.columnconfigure(0, weight=3)
        options.columnconfigure(1, weight=1)
        options.rowconfigure(0, weight=1)
        options.pack(pady=15, padx=10, fill="both")

        for report in self.reports:
            radio = ctk.CTkRadioButton(master=options, text=self.reports[report]["name"], variable=report_num, value=report)
            radio.grid(row=report-1, column=0, sticky=ctk.W, padx=20, pady=7)

        for export in self.exportation_types:
            radio = ctk.CTkRadioButton(master=options, text=self.exportation_types[export], variable=exportation, value=export)
            radio.grid(row=export-1, column=1, sticky=ctk.W, rowspan=4, padx=15, pady=7)

        description_frame = ctk.CTkFrame(master=frame)
        description_frame.pack(pady=15, padx=10, fill="both")

        title_description = ctk.CTkLabel(master=description_frame, text="Descripcion:", font=("Arial", 20))
        title_description.pack(pady=10, padx=10, anchor=ctk.W)

        description = ctk.CTkLabel(master=description_frame, textvariable=report_description, font=("Arial", 15), wraplength=740, justify=ctk.LEFT)
        description.pack(pady=10, padx=10, anchor=ctk.W)

        button = ctk.CTkButton(master=frame, text="Generar", command=callback, font=("Arial", 30))
        button.pack(pady=7, padx=10)

        root.update_idletasks()
        root.mainloop()
