from matplotlib.backends.backend_pdf import PdfPages
from construct.construct_1 import construct as c1
from construct.construct_2 import construct as c2
from construct.construct_3 import construct as c3
from construct.construct_4 import construct as c4
from construct.construct_5 import construct as c5
from construct.construct_6 import construct as c6
from construct.construct_7 import construct as c7

import matplotlib.pyplot as plt
from transform.transform import transform_report_one
import matplotlib

matplotlib.use("agg")

def create_report(selected_report, export_type):

    filename = f'reports/{selected_report}.{export_type}'

    if selected_report == "report1":
        c1().savefig(filename)

    elif selected_report == "report2":
        c2().savefig(filename)

    elif selected_report == "report3":
        c3().savefig(filename)

    elif selected_report == "report4":
        c4().savefig(filename)

    elif selected_report == "report5":
        c5().savefig(filename)

    elif selected_report == "report6":
        c6().savefig(filename)

    elif selected_report == "report7":
        c7().savefig(filename)

    else:
        return
            