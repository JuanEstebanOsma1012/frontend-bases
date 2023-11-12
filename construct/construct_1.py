import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from transform.transform import transform_report_one
import matplotlib

def construct():

    labels, values = transform_report_one()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis("equal")
    plt.title("Courses by schedule")

    return plt