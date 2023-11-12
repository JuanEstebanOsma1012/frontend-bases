from matplotlib.backends.backend_pdf import PdfPages
from construct.construct_1 import construct as construct_1
from construct.construct_2 import construct as construct_2
from construct.construct_3 import construct as construct_3
from construct.construct_4 import construct as construct_4
from construct.construct_5 import construct as construct_5
from construct.construct_6 import construct as construct_6
from construct.construct_7 import construct as construct_7


def create_report_one():
    with PdfPages(f"report1.pdf") as pdf:
        pdf.savefig(construct_1())
        pdf.close()

def create_report_two():
    with PdfPages("report2.pdf") as pdf:
        pdf.savefig(construct_2())
        pdf.close()

def create_report_three():
    with PdfPages("report3.pdf") as pdf:
        pdf.savefig(construct_3())
        pdf.close()

def create_report_four():
    with PdfPages("report4.pdf") as pdf:
        pdf.savefig(construct_4())
        pdf.close()

def create_report_five():
    with PdfPages("report5.pdf") as pdf:
        pdf.savefig(construct_5())
        pdf.close()

def create_report_six():
    with PdfPages("report6.pdf") as pdf:
        pdf.savefig(construct_6())
        pdf.close()

def create_report_seven():
    with PdfPages("report7.pdf") as pdf:
        pdf.savefig(construct_7())
        pdf.close()