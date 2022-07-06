from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage

def with_pdf (pdf_doc, pdf_pwd, fn, *args):
"""Open the pdf document, and apply the function, returning the results"""
result = None
try:
# open the pdf file
fp = open(pdf_doc, 'rb')
# create a parser object associated with the file object
parser = PDFParser(fp)
# create a PDFDocument object that stores the document structure
doc = PDFDocument()
# connect the parser and document objects
parser.set_document(doc)
doc.set_parser(parser)
# supply the password for initialization
doc.initialize(pdf_pwd)
if doc.is_extractable:
# apply the function and return the result
result = fn(doc, *args)
# close the pdf file
fp.close()
except IOError:
# the file doesn't exist or similar problem
pass
return result

