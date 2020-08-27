SET DATADIR=..\..\Cortex-Command-Community-Project-Data

rem python -m pip install openpyxl
python.exe ApplyBalance.py %DATADIR% Base.rte example_balance.csv
