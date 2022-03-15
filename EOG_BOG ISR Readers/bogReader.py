import pandas as pd
import numpy as np
import pathlib
from pathlib import Path
import PyPDF2
import re
from typing import List


def ISR_Reader(file_path:str, file_list:List[str]):
    file_path = Path(file_path)
    for f in file_list:
        pdfFileObj = open(file_path / f, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        df1= pd.DataFrame({'school':[], 'state_ID':[], 'name':[], 'grade':[], 'score':[], 'level':[]})
        for i in range(pdfReader.numPages):
            try:
                pageObj = pdfReader.getPage(i)
                school=re.search('School Name: (.+?)This'.replace('\s*',''),pageObj.extractText()).group(1)
                state_ID=re.search('Student ID: (.+?)Student Name:'.replace('\s*',''),pageObj.extractText()).group(1)
                name=re.search('Student Name: (.+?)Process Date:'.replace('\s*',''),pageObj.extractText()).group(1)
                grade=re.search('Grade (.+?)Student ID:'.replace('\s*',''),pageObj.extractText()).group(1)[0]
                try:
                    score=re.search('Scale Score (.+?)Students'.replace('\s*',''),pageObj.extractText()).group(1)
                except AttributeError:
                    score="NA"
                try:
                    level=re.search('Level (.+?)Scale Score'.replace('\s*',''),pageObj.extractText()).group(1)
                except AttributeError:
                    level="NP"
                df1.loc[len(df1)]=[school, state_ID, name, grade, score, level] 
            except AttributeError:
                next
        df1.to_csv(file_path / f"BOG_ISR_Read_G{f[25]}.csv", sep=",")
