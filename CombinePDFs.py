import PyPDF2

# Configuration
pdf1Name = 'Test pdf1.pdf'
pdf2Name = 'Test pdf2.pdf'
combinedPdfName = 'Combined pdf.pdf'

# Open the first PDF file
pdf1 = PyPDF2.PdfReader(open(pdf1Name, 'rb'))

# Open the second PDF file
pdf2 = PyPDF2.PdfReader(open(pdf2Name, 'rb'))

# Create a new PDF file
pdf_writer = PyPDF2.PdfWriter()

# Add the pages of the first PDF to the output file
for page in range(len(pdf1.pages)):
    pdf_writer.add_page(pdf1.pages[page])

# Add the pages of the second PDF to the output file
for page in range(len(pdf2.pages)):
    pdf_writer.add_page(pdf2.pages[page])

# Save the combined PDF to a file
with open(combinedPdfName, 'wb') as out:
    pdf_writer.write(out)
