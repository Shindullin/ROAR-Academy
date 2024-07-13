import PyPDF2 
file_handle = open( 'Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 
page_object = pdfReader.pages[0]    # We just get page 0 as example 
page_text = page_object.extractText()   # this is the str type of full page