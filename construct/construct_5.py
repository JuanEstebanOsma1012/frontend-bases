import matplotlib.pyplot as plt
from transform.transform import transform_report_five
 
def construct():

    x_labels, y_labels = transform_report_five()

    plt.plot(x_labels, y_labels, marker="o")
    plt.ylim(0, 5.0)
    plt.gcf().set_size_inches(9, 7)
    plt.show()