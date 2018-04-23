@echo Converting...
@echo off
:: set the path of the folder containing the .vnt files to be converted
set vPath=C:\Users\Vnotes
py -3 %~dp0vntParser.py --inputfolder %vPath% --outputfolder %vPath%\..\Txt