# PDF Reader Snippets

PDF to Object
```
import PyPDF2

pdfFileObj = open(path, "rb")
pdfReader=PyPDF2.PdfFileReader(pdfFileObj) # PDF Object

pdfReader.getPage(pageNumber) # Page object

pdfReader.getPage(pageNumber).extractText() # Text of single page object
```

Merge All Text
```
import os
import PyPDF2

def mergeText(path:str):
    allPages = ""   
    
    for file in [x for x in os.listdir(myDir/"Target") if x.endswith(".pdf")]:
        pdfFileObj = open(path/"Target"/file, "rb")
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        
        docPages = ""
        
        for x in range(pdfReader.numPages):
            docPages=docPages+str(pdfReader.getPage(x).extractText())
        
        allPages = allPages+docPages
    
    return allPages  
```

