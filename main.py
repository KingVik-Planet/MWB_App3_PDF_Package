from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()

    #Header guidelines
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 10, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 20, 200, 20)

    #Footer guidelines
    pdf.ln(260)

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(20, 20, 200)
    pdf.cell(w=0, h=10, txt=row['Topic'], align= "R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #Footer Guidelines
        pdf.ln(272)

        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(20, 20, 200)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("Kingsley.pdf")