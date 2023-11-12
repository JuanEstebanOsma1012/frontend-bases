import numpy as np
import matplotlib.pyplot as plt
from transform.transform import transform_report_three

def construct():

    x_labels, y_labels, values = transform_report_three()

    fig, ax = plt.subplots()
    ax.imshow(values)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(x_labels)), labels=x_labels)
    ax.set_yticks(np.arange(len(y_labels)), labels=y_labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(y_labels)):
        for j in range(len(x_labels)):
            ax.text(j, i, values[i, j],
                        ha="center", va="center", color="w")

    ax.set_title("Quices quantity by Topic and Teachers")
    fig.tight_layout()
    plt.show()