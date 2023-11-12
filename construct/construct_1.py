import matplotlib.pyplot as plt
from transform.transform import transform_report_one

def construct():

    labels, values = transform_report_one()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis("equal")
    plt.title("Courses by schedule")
    plt.show()
    
    # don't function yet
    # return plt.figure()