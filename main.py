from fpdf import FPDF

pdf = FPDF(orientation= "P", unit="mm", format= "A4")

pdf.add_page()
pdf.set_font(family="Arial",style= "B", size = 12)
pdf.cell(w=0, h= 12, txt = "Hi Kingsley", align="L", ln =1, border=1)

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