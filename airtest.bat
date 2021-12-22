@echo off

::set artestProDir=%cd%\ide\AirtestIDE_2020-01-21_py3_win64\AirtestIDE.exe
color 2

set rootPaht=%cd%

set scriptPath=%rootPaht%\scripts\runGame.air

title  runGame.air  %2  %packName%


choice /t 20 /d y /n >nul

::pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com airtest


::%artestProDir% runner %scriptPath% --device Android://%1
::airtest run %scriptPath% --device Android://%1

python -m airtest run %scriptPath% --device Android://%1
