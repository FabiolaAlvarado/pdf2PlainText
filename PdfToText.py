import pdftotext
class Pdf:
    
 with open("Lorem_ipsum.pdf", "rb") as myFile:
    pdf = pdftotext.PDF(myFile)
    
 print("\n\n".join(pdf))