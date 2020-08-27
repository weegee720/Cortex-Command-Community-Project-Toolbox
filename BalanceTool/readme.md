!!! ALWAYS COMMIT YOUR INIs BEFORE USING THIS TOOL SO YOU CAN ROLL BACK IF IT GLITCHES !!!  
  
This tool is crated to simplify major balance work. You can apply a set of value changes to the entities in the entire RTE module, or even a few at once.  
  
Values must be present in the INI file, non existing values won't be added!  
  
Accepts CSV and XLSX files as balance sheets. Use provided example files as templates.  
  
Tool alters your INI files, so make sure you can roll back these changes. Commit your work before using the tool!  
  
Use provided batch files and balance files as reference.  
  
Install openpyxl using *python -m pip install openpyxl*  
  
USAGE: ApplyBalance.py <data_directory> <module_name> <balance_csv_or_xlsx_file>  
  
EXAMPLE: ApplyBalance.py ..\..\Cortex-Command-Community-Project-Data Base.rte example_balance.xlsx  
  
