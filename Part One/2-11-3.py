import PyPDF2 
import os
import string
import time

start_time= time.time()
path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, 'Sense_and_Sensibility-by-Jane-Austen.pdf')
file_handle = open(file_path, 'rb')
pdfReader = PyPDF2.PdfReader(file_handle) 

frequency_table = {}

for page_num in range(len(pdfReader.pages)):
    page_object=pdfReader.pages(page_num)
    page_text = page_object.extrace_text()
    words=page_text.split("\n")
    placeholder_char=""
    for extracted_string in words:
        if extracted_string=="page" or extracted_string=="CHAPTER":
            extracted_string==""
        list_of_string=extracted_string.split("\n")
        for char in list_of_string:
            if char=="." or "/":
                char=""
            if char.isdigit():
                char=""
        word=''.join(list_of_string)        
        if word in frequency_table:
            frequency_table[word]+=1
        else:
            frequency_table[word] = 1

print(frequency_table)
