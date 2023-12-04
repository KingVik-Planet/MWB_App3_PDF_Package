from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation= "P", unit="mm", format= "A4")

df = pd.read_csv("topic.csv")
pdf.add_page()


pdf.set_font(family="Arial",style= "B", size = 12)
text = (" Streamlit makes it easy for you to visualize, mutate, and share data\n. \n"
        "        The API reference is organized by activity type, like displaying data \n"
        "        or optimizing performance. Each section includes methods associated with \n"
        "        the activity type, including examples.")

pdf.cell(w=0, h= 12, txt = text, align="L", ln =1, border=1)

pdf.set_font(family="Times",style= "BI", size = 12)
pdf.cell(w=0, h= 12, txt = "How are you", align="C", ln =1, border=1)

pdf.set_font(family="Helvetica",style= "B", size = 12)
pdf.cell(w=0, h= 12, txt = "Kingsley Chika CHUKWU", align="R", ln =1, border=1)


pdf.add_page()
pdf.set_font(family="Arial",style= "B", size = 12)
pdf.cell(w=0, h= 12, txt = "Hi Kingsley, this is me to you", align="L", ln =1, border=1)

pdf.set_font(family="Times",style= "B", size = 12)
pdf.cell(w=0, h= 12, txt = "How are you, Hopefully I know you are doing great", align="C", ln =1, border=1)

pdf.set_font(family="Helvetica",style= "B", size = 12)
pdf.cell(w=0, h= 12, txt = "Kingsley Chika CHUKWU, This is the last text in the second page", align="R", ln =1, border=1)

pdf.output("Kingsley.pdf")