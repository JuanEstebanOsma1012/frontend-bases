import matplotlib.pyplot as plt
from transform.transform import transform_report_seven
 
def construct():

    x_labels, left_y_labels, right_y_labels = transform_report_seven()

    figure, axis = plt.subplots()
    axis.bar(x_labels, left_y_labels, color="steelblue")
    axis2 = axis.twinx()
    axis2.plot(x_labels, right_y_labels, color="red", marker="o", ms=5)

    axis.tick_params(axis='y', colors="steelblue")
    axis2.tick_params(axis='y', colors="red")
    plt.show()