import csv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

csv_file = "sample_data.csv"

names = []
scores = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row["Name"])
        scores.append(int(row["Score"]))

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

pdf_file = "student_report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Student Performance Report", styles["Title"]))

elements.append(Paragraph(f"Average Score: {average_score}", styles["Normal"]))
elements.append(Paragraph(f"Highest Score: {highest_score}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Score: {lowest_score}", styles["Normal"]))


table_data = [["Name", "Score"]]
for name, score in zip(names, scores):
    table_data.append([name, score])

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (1, 1), (-1, -1), "CENTER")
]))

elements.append(table)


doc.build(elements)

print("PDF report generated successfully!")
