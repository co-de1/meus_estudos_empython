# Modulos externos

"""
Para instalar um modulo externo fazemos:

pip <instrução> [package]

EXemplo: pip install pypdf

from pypdf import PdfReader

reader = PdfReader("ROADMAP BACK-END.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

"""
