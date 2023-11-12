from fetch.fetch import load_report_data
import numpy as np

def transform_report_one():

    plain_data = load_report_data(1)

    labels = []
    values = []
    for block in plain_data:
        labels.append(f'{block["hora_inicio"]}-{block["hora_fin"]}')
        values.append(block["n_grupos"])

    return labels, values

def transform_report_two():

    plain_data = load_report_data(2)

    labels = []
    values = []
    for block in plain_data:
        labels.append(block["tipo_pregunta"])
        values.append(block["n_preguntas"])

    return labels, values

def transform_report_three():

    plain_data = load_report_data(3)

    x_labels = plain_data["materias"]
    y_labels = plain_data["profesores"]
    values = np.array(plain_data["heatmap_n_quices"])

    return x_labels, y_labels, values

def transform_report_four():

    plain_data = load_report_data(4)

    x_labels = plain_data["temas"]
    y_labels = plain_data["grupos"]
    values = np.array(plain_data["heatmap_calificacion_promedio"])

    return x_labels, y_labels, values

def transform_report_five():

    plain_data = load_report_data(5)
    x_labels = plain_data["meses"]
    y_labels = plain_data["calificacion_promedio"]

    return x_labels, y_labels

def transform_report_six():

    plain_data = load_report_data(6)
    x_labels = plain_data["meses"]
    y_labels = plain_data["cantidad_quices"]

    return x_labels, y_labels

def transform_report_seven():

    plain_data = load_report_data(7)

    x_labels = plain_data["profesores"]
    left_y_labels = plain_data["n_bancos"]
    right_y_labels = plain_data["n_preguntas_promedio"]

    return x_labels, left_y_labels, right_y_labels
