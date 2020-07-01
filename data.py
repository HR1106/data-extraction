import io
from PIL import Image
import fitz
import pytesseract
file=fitz.open("39_Previous_Papers_Indian_History_CSAT_Paper_I_Civil_Services_Exam.pdf")
page=len(file)
for i in range(2,page):
  for image in file.getPageImageList(i):
    j=0
    customxref=image[0]
    pic=fitz.Pixmap(file,customxref)
    finalpic=fitz.Pixmap(fitz.csRGB,pic)
    finalpic.writePNG(str(i)+".png")
    pic=None
    finalpic=None
outfile = "out_text.txt"
f = open(outfile, "a")
for i in range(2,page):  
    filename = str(i)+".png"
           
    text = str(((pytesseract.image_to_string(Image.open(filename)))))  
  
    f.write(text)
f.close()
