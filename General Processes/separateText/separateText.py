import os
import PyPDF2
from termcolor import colored
from pathlib import Path

myDir = Path(os.path.dirname(os.path.realpath(__file__)))

def mergeText(path:str):
    allPages = ""   
    
    for file in [x for x in os.listdir(myDir/"Target") if x.endswith(".pdf")]:
        pdfFileObj = open(path/"Target"/file, "rb")
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        
        docPages = ""
        
        for x in range(pdfReader.numPages):
            docPages=docPages+str(pdfReader.getPage(x).extractText())
        
        allPages = allPages+docPages
        
        print(f"Reading file: {colored(file, 'cyan')}\n.............................................................\n\n", docPages)
        
        with open(path/"Output"/file.replace(".pdf", ".txt"), "w", encoding="utf-8") as textBlock:
            textBlock.write(docPages)
            
    with open(path/"Output"/"fullOutput.txt", "w", encoding="utf-8") as textBlock:
        textBlock.write(allPages)    
                
mergeText(myDir)
