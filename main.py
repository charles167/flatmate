from flat import Bill, Flatmate
from reports import PdfReport


# Ask for user input
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. March 2025: ")

name1 = input("What is your name? ")
days1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

# Create objects
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days1)
flatmate2 = Flatmate(name2, days2)

# Print results
print(f"{flatmate1.name} pays: ${flatmate1.pays(the_bill, flatmate2)}")
print(f"{flatmate2.name} pays: ${flatmate2.pays(the_bill, flatmate1)}")

# Generate PDF
pdf_report = PdfReport(filename=f"Bill_{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
