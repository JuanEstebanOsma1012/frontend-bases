import matplotlib.pyplot as plt
from transform.transform import transform_report_seven
 
def construct():

    x_labels, left_y_labels, right_y_labels = transform_report_seven()

    figure, axis = plt.subplots()
    axis.bar(x_labels, left_y_labels, color="steelblue")

    axis.set_ylabel("Cantidad de bancos", color="steelblue")
    axis.set_xlabel("Profesores")
    axis.set_title("Cantidad de bancos y preguntas promedio por profesor")

    axis2 = axis.twinx()
    axis2.plot(x_labels, right_y_labels, color="red", marker="o", ms=5)
    axis2.set_ylabel("Cantidad de preguntas promedio por banco", color="red")

    axis.tick_params(axis='y', colors="steelblue")
    axis2.tick_params(axis='y', colors="red")
    
    return plt