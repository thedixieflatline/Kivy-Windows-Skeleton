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
set PYTHONPATH=%PYTHONPATH%;C:\Users\david\Documents\slotsim
echo %PYTHONPATH%
echo.
echo ACTIVATE PYTHON VIRTUALENV and START GAME
echo.
cmd /k "cd /d C:\Users\david\Documents\slotsim\Scripts\ & activate & cd /d C:\Users\david\Documents\slotsim\share\kivy-examples\demo\showcase\ & python main.py runserver"
echo.
echo -------------
echo SLOTSIM STARTING