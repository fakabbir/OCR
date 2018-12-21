"""OCR extractor from hOCR file generated from tesseract

This script allows the user to extract business important fields
such as invoice number, invoice date, total amount.

It is assumed that the hOCR is the most pure / accurate form of result
and extra pre processing to correct the detection is required.

However result cleaning has been taken care.

Note and Disclaimer:

This code is by no means any replacement to OCR already been used at your bay.
I have written it from scratch without grabbing important functionality from the web.

The code is by no means meant to be highly robust, plug and play, efficent.
This has been done intentionally to avoid headache.
"""

from config.KEYS import *
from OCRUtils import *

filePathList = []
filePathList.append('../OCR_Output_For_Sample_Invoices/1_100A 39015.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/2_215B 72.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/3_AD Notions Int\'l Pte Ltd.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/4_Sample 5.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/5_CIOX_0248727220.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/6_ORAC 44273107.pdf.xml')
filePathList.append('../OCR_Output_For_Sample_Invoices/7_1120V 5568.pdf.xml')


for filePath in filePathList:

    textBlob = gettextBlob(filePath)
    print("Extraction for file: ",filePath)
    print("------------------------")

    # Invoice Number
    possibleKey = KeyCandidates(textBlob,KEY_INVOICE_NUMBER)
    isPresent_ = isPresent(possibleKey,"INVOICE_NUMBER")
    if isPresent_[0]:
        print("Number: ",isPresent_[1])
    else:
        print("Number: ",extractFromNear(textBlob,possibleKey,"INVOICE_NUMBER","LEFT"))

    # Date:
    possibleKey = KeyCandidates(textBlob,KEY_INVOICE_DATE)
    isPresent_ = isPresent(possibleKey,"INVOICE_NUMBER")
    if isPresent_[0]:
        print("Date: ",isPresent_[1])
    else:
        print("Date: ",extractFromNear(textBlob,possibleKey,"INVOICE_DATE","LEFT"))

    #Amount:
    possibleKey = KeyCandidates(textBlob,KEY_AMOUNT)
    isPresent_ = isPresent(possibleKey,"INVOICE_AMOUNT")
    if isPresent_[0]:
        print("Amount: ",isPresent_[1])
    else:
        print("Amounnt: ",extractFromNear(textBlob,possibleKey,"INVOICE_NUMBER","LEFT"))

    #Terms:
    possibleKey = KeyCandidates(textBlob,KEY_TERMS)
    isPresent_ = isPresent(possibleKey,"INVOICE_AMOUNT")
    if isPresent_[0]:
        print("Terms: ",isPresent_[1])
    else:
        print("Terms: ",extractFromNear(textBlob,possibleKey,"INVOICE_NUMBER","LEFT"))
