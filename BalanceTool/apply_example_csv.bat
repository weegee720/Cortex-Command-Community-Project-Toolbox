SET DATADIR=..\..\Cortex-Command-Community-Project-Data

rem python -m pip install openpyxl
python.exe ApplyBalance.py %DATADIR% Base.rte 
rem example_balance.csv
