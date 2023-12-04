from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation= "P", unit="mm", format= "A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
        pdf.add_page()

        pdf.set_font(family="Helvetica",style= "B", size = 25)
        pdf.set_text_color(r=100, g=10, b=100)
        pdf.cell(w=0, h= 12, txt = row["Topic"], align="L", ln =1, border=0)
        pdf.line(x1=10, y1=20, x2=200, y2=20)

pdf.output("Kingsley.pdf")