import pandas as pd
import numpy as np
import pathlib
from pathlib import Path
import PyPDF2
import re
from typing import List

schName = re.compile(r"(?<=School Name: )(.*)(?=The goal)".replace(r'\s*', ''))
stuID = re.compile(r"(?<=Student ID: )(.+?)(?=Student Name:)".replace(r'\s*', ''))
stuName = re.compile(r"(?<=Student Name: )(.+?)(?=Process Date:)".replace(r'\s*', ''))
stuGrade = re.compile(r"(?<=Grade )(.+?)(?= Reading TestStudent ID:)".replace(r'\s*', ''))
stuScale = re.compile(r"(?<=Scale Score )(.{3})".replace(r'\s*', ''))
stuLvl = re.compile(r"(?<=isr Beginning-of-Grade 3 Reading )(.*?)(?=Scale Score)".replace(r'\s*', ''))



def ISR_Reader(file_path:str, file_list:List[str]):
    file_path = Path(file_path)
    for f in file_list:
        pdfFileObj = open(file_path / f, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        df1 = pd.DataFrame({'school':[], 'state_ID':[], 'name':[], 'grade':[], 'score':[], 'level':[]})
        for i in range(pdfReader.numPages):
            try:
                pageObj = pdfReader.getPage(i)
                school = schName.search(pageObj.extractText())[0]
                state_ID = stuID.search(pageObj.extractText())[0]
                name = stuName.search(pageObj.extractText())[0]
                grade = stuGrade.search(pageObj.extractText())[0]
                try:
                    score = stuScale.search(pageObj.extractText())[0]
                except AttributeError:
                    score = "NA"
                try:
                    level = stuLvl.search(pageObj.extractText())[0]
                except AttributeError:
                    level = "NP"
                df1.loc[len(df1)]=[school, state_ID, name, grade, score, level] 
            except AttributeError:
                next
        df1.to_csv(file_path / f"BOG_ISR_Read_G{f[25]}.csv", sep=",")
