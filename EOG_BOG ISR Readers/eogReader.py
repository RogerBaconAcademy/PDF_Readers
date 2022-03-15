import pandas as pd
import numpy as np
import os
import time
import datetime
import pathlib
from pathlib import Path
import PyPDF2
import re
from typing import List



def ISR_Reader(file_path:str, file_list:List[str]):
    df2=pd.DataFrame({'school':[], 'test':[], 'state_ID':[], 'name':[], 'grade':[], 'score':[], 'level':[]})
    for f in [x for x in file_list if x.endswith(".pdf")]:
        pdfFileObj = open(file_path / f, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        df1= pd.DataFrame({'school':[], 'test':[], 'state_ID':[], 'name':[], 'grade':[], 'score':[], 'level':[]})
        for i in range(pdfReader.numPages):
            try:
                pageObj = pdfReader.getPage(i)
                school=re.search('School Name: (.+?)This'.replace('\s*',''),pageObj.extractText()).group(1)
                state_ID=re.search('Student ID: (.+?)Student Name:'.replace('\s*',''),pageObj.extractText()).group(1)
                name=re.search('Student Name: (.+?)Process Date:'.replace('\s*',''),pageObj.extractText()).group(1)
                try:
                    grade=re.search('Grade (.+?)Student ID:'.replace('\s*',''),pageObj.extractText()).group(1)[0]
                except AttributeError:
                    grade=re.search('Grade: (.+?)Student ID:'.replace('\s*',''),pageObj.extractText()).group(1)[0]
                try:
                    test=re.search('administered End-of-Grade (.+?) test'.replace('\s*',''),pageObj.extractText(), re.IGNORECASE).group(1)
                except AttributeError:
                    try:
                        test=re.search('administered End-of-Course (.+?)test'.replace('\s*',''),pageObj.extractText(), re.IGNORECASE).group(1)
                    except AttributeError:
                        test=re.search('recently administered (.+?)test'.replace('\s*',''),pageObj.extractText(), re.IGNORECASE).group(1)
                try:
                    score=re.search('Scale Score (.+?)Students'.replace('\s*',''),pageObj.extractText()).group(1)
                except AttributeError:
                    score="NA"
                try:
                    level=re.search('Level (.+?)Scale Score'.replace('\s*',''),pageObj.extractText()).group(1)
                except AttributeError:
                    level="NP"
                df1.loc[len(df1)]=[school.strip(), test.strip(), state_ID.strip(), name.strip(), grade.strip(), score.strip(), level.strip()] 
            except AttributeError:
                next
        df2=df2.append(df1, ignore_index=True)
    df2.to_csv(file_path / "EOG_ISR_All.csv", sep=",")