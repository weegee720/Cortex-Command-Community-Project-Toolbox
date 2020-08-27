SET DATADIR=..\..\Cortex-Command-Community-Project-Release

python.exe MergeDataModule.py %DATADIR% Base.rte
python.exe MergeDataModule.py %DATADIR% Dummy.rte
python.exe MergeDataModule.py %DATADIR% Coalition.rte
python.exe MergeDataModule.py %DATADIR% Browncoats.rte
python.exe MergeDataModule.py %DATADIR% Imperatus.rte
python.exe MergeDataModule.py %DATADIR% Ronin.rte
python.exe MergeDataModule.py %DATADIR% Techion.rte
python.exe MergeDataModule.py %DATADIR% Missions.rte
