@echo off 
echo SLOTSIM WINDOWS START
echo -------------
echo.
echo SET PYTHON PATH
echo.
set PATH=C:\Program Files (x86)\Python36-32;%PATH%
echo %PATH%
echo.
echo SET PYTHON VIRTUALENV PATH
echo.
rem s%~dp0 is the folder relative to where this script started and is equivilant to PYTHONPATH=%PYTHONPATH%;C:\Users\username\Documents\pathtothisgitcheckoutfolder
set PYTHONPATH=%PYTHONPATH%;%~dp0
echo %PYTHONPATH%
echo.
echo ACTIVATE PYTHON VIRTUALENV and START GAME
echo.
cmd /k "cd /d %~dp0\Scripts\ & activate & cd /d %~dp0 & python main.py runserver"
echo -------------
echo SLOTSIM STARTING
pause
