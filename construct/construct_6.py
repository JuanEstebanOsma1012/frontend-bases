import matplotlib.pyplot as plt
from transform.transform import transform_report_six
 
def construct():

    x_labels, y_labels = transform_report_six()

    plt.plot(x_labels, y_labels, marker="o")
    plt.tick_params(axis='x', which='major', labelsize=8, rotation=90)
    plt.gcf().set_size_inches(9, 7)

    plt.title("Cantidad de quices puestos a lo largo del tiempo (basado en su fecha de finalizacion)")
    plt.xlabel("Meses")
    plt.ylabel("Cantidad de quices")
    
    return plt