#ref : https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/
import img2pdf
from PIL import Image
import os
import sys
 


def convert_img_2_pdf(img_path=None,pdf_path=None):
    # opening image
    image = Image.open(img_path)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    
    # opening or creating pdf file
    file = open(pdf_path, "wb")
    
    # writing pdf files with chunks
    file.write(pdf_bytes)
    
    # closing image file
    image.close()
    
    # closing pdf file
    file.close()
 
    # output
    print("Successfully made pdf file")

if __name__=="__main__":
    if len(sys.argv)<2:
        print("please provide img path")
        sys.exit(1)
    pdfPath=None
    try :
        pdfPath =sys.argv[2]
    except :
        pdfPath="./output.pdf"
    convert_img_2_pdf(sys.argv[1],pdfPath)