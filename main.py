from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation= "P", unit="mm", format= "A4")

df = pd.read_csv("topic.csv")

for index, row in df.iterrows():
        pdf.add_page()

        pdf.set_font(family="Helvetica",style= "B", size = 12)
        pdf.set_text_color(r=100, g=100, b=100)
        pdf.cell(w=0, h= 12, txt = "Kingsley Chika CHUKWU", align="R", ln =1, border=1)
        pdf.line(x1=10, y1=20, x2=200, y2=20)



pdf.output("Kingsley.pdf")