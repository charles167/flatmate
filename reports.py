from fpdf import FPDF
import webbrowser


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font("Arial", "B", 24)
        pdf.cell(0, 40, "Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 20, f"Period: {bill.period}", ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 20, f"{flatmate1.name} pays: ${flatmate1.pays(bill, flatmate2)}", ln=1)
        pdf.cell(0, 20, f"{flatmate2.name} pays: ${flatmate2.pays(bill, flatmate1)}", ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
