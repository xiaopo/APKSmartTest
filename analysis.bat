@echo off

title analysis %1   %packName%
color 3


:start_pull_data
echo #############################send data to pc

choice /t 20 /d y /n >nul

set outPath=%outDataPath%\%1\
if exist %outPath% (
	echo ....................
) else (
	md %outPath%
)

adb -s %1 pull %folder%profile.data %outPath% 

choice /t 1 /d y /n >nul

set gameName=Éñ¶¼·üÄ§Â¼

if exist %outPath%\profile.data %SavePath%\exe\GameProfilerLoad.exe %outPath%\profile.data
	
if exist %outPath%\profile.csv %SavePath%\exe\CSVToJson.exe %outPath%\profile.csv %gameName% %1

goto :start_pull_data

