# **separateText**

This programm is designed to scrape text content from all of the PDF files within the `Target` folder and write them as `.txt` files into the `Output` folder. The `Ouput` folder will contain one text file for each PDF plus one for the combined text of all processed files. Before use it is best practice to ensure the `Output` folder is clear of files, and that `Target` contains only the PDF's to be processed. 

## Windows Users
May execute the program by simply running the enclosed batch file:
```
run_sepTxt
```
*OR*
```
python -m venv myPy_env
myPy_env\Scripts\activate.bat
pip install -r requirements.txt
python separateText.py
```

## Unix Users
```
python3 -m venv myPy_env
source myPy_env/bin/activate
pip install -r requirements.txt
python3 separateText.py
```
_____________________________

Requires:
- [Python 3.8](https://www.python.org/downloads/release/python-3810/)
- [venv](https://docs.python.org/3/library/venv.html)
