cd /D "%~dp0" && ^
if exist sepTxt_env\ (sepTxt_env\Scripts\activate.bat && python separateText.py) else (python -m venv sepTxt_env && pip install -r requirements.txt && sepTxt_env\Scripts\activate.bat && timeout 4 && python separateText.py)
