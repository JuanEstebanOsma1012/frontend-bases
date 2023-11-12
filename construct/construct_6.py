import matplotlib.pyplot as plt
from transform.transform import transform_report_six
 
def construct():

    x_labels, y_labels = transform_report_six()

    plt.plot(x_labels, y_labels, marker="o")
    plt.gcf().set_size_inches(9, 7)
    plt.show()