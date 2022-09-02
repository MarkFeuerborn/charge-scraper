import os
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pathlib import Path


def parsePdf(filename):

    dataDir = Path(r'/home/pi/Scraper/Output')

    with open(dataDir/filename, 'rb') as pdfFileObj:
        #The pdfReader variable is a readable object that will be parsed.
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

    #Discerning the number of pages will allow us to parse through all the pages.
        num_pages = pdfReader.numPages
        count = 0
        text = ""

    #The while loop will read each page.
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()

    #This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
        if text != "":
            text = text
    #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
        else:
            text = textract.process(filename, method='tesseract', language='eng')
    #Now we have a text variable that contains all the text derived from our PDF file.

    #The word_tokenize() function will break our text phrases into individual words.
        tokens = word_tokenize(text)

    #We make a list of words we want to find in the document and create an empty list for comparison
        interested_words = ['felonious', 'terroristic', 'battery', 'murder', 'rape', 'impersonating', 'document', 'test']
        testList = []

    #We compare the tokens and interested_words list and add any words that match to the testList to return
        for x in tokens:
            for y in interested_words:
                if x.lower() == y:
                    testList.append(x)

        print(testList)
        print(filename)
        


        return (testList)

#for testing
filename = "FCMC Arraignment Report 4D 2022-09-02.pdf?879897"
parsePdf(filename)
