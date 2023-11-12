import dearpygui.dearpygui as dpg
from export.export import create_report as cr

selected_report = ""

def create_report(export_type):
    cr(selected_report, export_type)

# CALLBACK
def export(sender, data):

    create_report(sender)

    dpg.hide_item("Export Type")
    dpg.show_item("Reports Manager")

# CALLBACK
def generate_report(sender, data):
    
    global selected_report
    selected_report = sender
    export_type = select_export_type()

def select_export_type():

    dpg.show_item("Export Type")
    dpg.hide_item("Reports Manager")

def initialize():

    dpg.create_context()
    dpg.create_viewport(title='Reports manager')

    with dpg.font_registry():
        title_font = dpg.add_font("Roboto-Light.ttf", 40)
        subtitle_font = dpg.add_font("Roboto-Light.ttf", 30)
        default_font = dpg.add_font("Roboto-Light.ttf", 25, default_font=True)

    with dpg.window(tag="Export Type", label="Tipo de exportacion", no_resize=True, no_move=True, no_collapse=True, no_close=True, no_background=True, no_bring_to_front_on_focus=True, no_title_bar=True, no_scrollbar=True, no_saved_settings=True, show=False):
        
        dpg.bind_font(default_font)

        # a centered text saying "Please select the export type"
        subtitle = dpg.add_text("Por favor seleccione un tipo de exportacion\n", parent="Export Type")
        dpg.bind_item_font(subtitle, subtitle_font)

        # a button for export to PDF
        dpg.add_button(tag="pdf", label="PDF", parent="Export Type", callback=export)

        # a button for export to PNG
        dpg.add_button(tag="png", label="PNG", parent="Export Type", callback=export)

        # a button for export to SVG
        dpg.add_button(tag="svg", label="SVG", parent="Export Type", callback=export)

        # a button for export to JPG
        dpg.add_button(tag="jpg", label="JPG", parent="Export Type", callback=export)

    with dpg.window(tag="Reports Manager", label="Gestor de reportes", no_resize=True, no_move=True, no_collapse=True, no_close=True, no_background=True, no_bring_to_front_on_focus=True, no_title_bar=True, no_scrollbar=True, no_saved_settings=True, show=True):
        
        dpg.bind_font(default_font)

        # a centered big text saying "Welcome to the Reports Manager"
        title = dpg.add_text("Bienvenido al gestor de reportes", parent="Reports Manager")
        dpg.bind_item_font(title, title_font)

        # a centered text smaller than the previous one saying "Please select a report to generate"
        subtitle = dpg.add_text("Por favor seleccione un reporte para generar\n", parent="Reports Manager")
        dpg.bind_item_font(subtitle, subtitle_font)

        # seven clickable groups with the name of the reports and his description, when i click on one of them, an modal window will appear for select the export type
        # the modal window will have a text saying "Please select the export type" and two buttons, one for export to PDF and another for export to PNG
        # the modal window will have a button for generate the report
        # the modal window will have a button for cancel the report generation
        # every subgroup has a line surrounding it
        with dpg.child_window(label="Report One", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Distribucion de cursos por horario", parent="Report One")
            dpg.add_text("Este reporte muestra una grafica de pastel que muestra la cantidad de cursos que hay en un horario en particular", parent="Report One")
            dpg.add_button(tag="report1", label="Generate", parent="Report One", callback=generate_report)

        with dpg.child_window(label="Report Two", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Distribucion de preguntas por tipo", parent="Report Two")
            dpg.add_text("Este grafico muestra la cantidad de preguntas que hay almacenadas en el sistema de cada tipo (seleccion multiple o abierta)", parent="Report Two")
            dpg.add_button(tag="report2", label="Generate", parent="Report Two", callback=generate_report)

        with dpg.child_window(label="Report Three", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Heatmap de Quices por tema y profesor", parent="Report Three")
            dpg.add_text("Este reporte muestra un grafico de calor que distribuye la cantidad de quices que hay de cada profesor en cada materia en particular", parent="Report Three")
            dpg.add_button(tag="report3", label="Generate", parent="Report Three", callback=generate_report)

        with dpg.child_window(label="Report Four", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Heatmap de calificacion por tema y grupo", parent="Report Four")
            dpg.add_text("Este reporte muestra un grafico de calor que distribuye la calificacion promedio de quices que hay de cada grupo en cada tema que se ve", parent="Report Four")
            dpg.add_button(tag="report4", label="Generate", parent="Report Four", callback=generate_report)

        with dpg.child_window(label="Report Five", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Desempeño estudiantil a lo largo del tiempo", parent="Report Five")
            dpg.add_text("Este reporte muestra el desempeño promedio estudiantil en cada mes", parent="Report Five")
            dpg.add_button(tag="report5", label="Generate", parent="Report Five", callback=generate_report)

        with dpg.child_window(label="Report Six", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Cantidad de quices a lo largo del tiempo", parent="Report Six")
            dpg.add_text("Este reporte muestra una linea de tiempo de la cantidad de quices que se han registrado basado en su fecha de finalizacion", parent="Report Six")
            dpg.add_button(tag="report6", label="Generate", parent="Report Six", callback=generate_report)

        with dpg.child_window(label="Report Seven", parent="Reports Manager", height=130, width=1250, border=True):
            dpg.add_text("Cantidad de bancos por profesor y cantidad de preguntas promedio por banco", parent="Report Seven")
            dpg.add_text("Este reporte muestra la cantidad de bancos que tiene registrados cada profesor y las preguntas promedio por cada banco de ese profesor, siendo la cantidad de quices el grafico de barras (eje izquierdo) y la cantidad de preguntas promedio por banco el grafico de linea (eje derecho)", parent="Report Seven")
            dpg.add_button(tag="report7", label="Generate", parent="Report Seven", callback=generate_report)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()