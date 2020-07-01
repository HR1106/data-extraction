import os
import pdfplumber

os.system(f'ocrmypdf --skip-text 39_Previous_Papers_Indian_History_CSAT_Paper_I_Civil_Services_Exam.pdf output.pdf')

with pdfplumber.open('output.pdf') as pdf:
  page=pdf.pages[3]
  text=page.extract_text()
  print(text)
