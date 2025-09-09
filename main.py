from flask import Flask, render_template, request
from flat import Bill, Flatmate
from reports import PdfReport

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from form
        amount = float(request.form["amount"])
        period = request.form["period"]

        name1 = request.form["name1"]
        days1 = int(request.form["days1"])

        name2 = request.form["name2"]
        days2 = int(request.form["days2"])

        # Create objects
        the_bill = Bill(amount, period)
        flatmate1 = Flatmate(name1, days1)
        flatmate2 = Flatmate(name2, days2)

        # Payments
        pay1 = flatmate1.pays(the_bill, flatmate2)
        pay2 = flatmate2.pays(the_bill, flatmate1)

        # Generate PDF
        pdf_report = PdfReport(filename=f"Bill_{the_bill.period}.pdf")
        pdf_report.generate(flatmate1, flatmate2, the_bill)

        return render_template(
            "result.html",
            name1=name1, pay1=pay1,
            name2=name2, pay2=pay2,
            period=period
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
