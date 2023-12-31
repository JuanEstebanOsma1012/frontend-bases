import matplotlib.pyplot as plt
from transform.transform import transform_report_five
 
def construct():

    x_labels, y_labels = transform_report_five()

    plt.plot(x_labels, y_labels, marker="o")
    plt.tick_params(axis='x', which='major', labelsize=8, rotation=90)
    plt.ylim(0, 100)
    plt.gcf().set_size_inches(9, 7)

    plt.title("Promedio de calificación por mes")
    plt.xlabel("Meses")
    plt.ylabel("Promedio de calificación")
    return plt