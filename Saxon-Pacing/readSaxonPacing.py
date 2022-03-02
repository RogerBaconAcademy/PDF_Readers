# imports
import pandas as pd
import numpy as np
import PyPDF2
import re
from termcolor import colored

# Document Reader
def find_vals(path:str):
    pdfFileObj = open(path, 'rb')
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

    allPages = ""
    for x in range(pdfReader.numPages):
        allPages=allPages+str(pdfReader.getPage(x).extractText())
    
    z = re.findall('LESSON(.+?)OBJECTIVES(.+?)Math Center',allPages.replace('\n', ' ').replace('•', '|'))  #specify functional regex
    
    lct = len(re.findall('LESSON', str(allPages))) #verification regex
    
    print(f"{path}\nLessons: {len(re.findall('LESSON', str(allPages)))}\nLessons Matched: {len(z)}\n\t{colored('Pass', 'green') if  lct==len(z) else colored('You may have missed values. Please verify regex!', 'red')}") #validate 
    
    
    ls = []
    for tup in z:
        ls.append([tup[0],'; '.join(tup[1].replace('™', "'").replace('ﬁ', '"').replace('ﬂ', '"').replace('Œ', '-').split('|'))])

    df = pd.DataFrame({'lesson_code':dict(ls).keys(), 'description':dict(ls).values()})
    df.description = df.description.apply(lambda x: x[2:].strip() if x.startswith(' ;') | x.startswith(';') else x.strip()) # remove leading ;
    df.description = df.description.apply(lambda x: x[:3].replace(' ', '')+x[3:]) # fix 'I dentify' disjointed leading word issue
    
    return df

df_k=find_vals('R:\\Data\\Data Dept\\Database\\Data Imports\\2021-22\\curriculum\Kinder Saxon Lesson Guide.pdf')
df_1=find_vals('R:\\Data\\Data Dept\\Database\\Data Imports\\2021-22\\curriculum\First Saxon Lesson Guide.pdf')
df_2=find_vals('R:\\Data\\Data Dept\\Database\\Data Imports\\2021-22\\curriculum\Second Saxon Lesson Guide.pdf')

# Add program code
df_k['program_code'] = 'Saxon K'
df_1['program_code'] = 'Saxon 1'
df_2['program_code'] = 'Saxon 2'

df_all = pd.concat([df_k, df_1, df_2], ignore_index=True) # stack data frames
df_all['sort_order'] = df_all.index+1  # Add sort order

# Export as tab separated
df_all.loc[:,['program_code', 'lesson_code', 'description', 'sort_order']].to_csv('R:\\Data\\Data Dept\\Database\\Data Imports\\2022-23\\curriculum\myFileName.csv', index=False, sep='\t')