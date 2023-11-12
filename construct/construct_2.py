import matplotlib.pyplot as plt
from transform.transform import transform_report_two

def construct():

    labels, values = transform_report_two()

    plt.pie(values, labels=labels, explode=[0.02 for i in labels], autopct='%1.1f%%', pctdistance=0.85)

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()

    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)

    # Adding Title of chart
    plt.title('Questions by type')

    # Displaying Chart
    plt.show()
