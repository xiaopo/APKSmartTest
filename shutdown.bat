@echo off

::É±ËÀ¶Ë¿Ú
REM for /f "delims=  tokens=1" %%i in ('netstat -aon ^| findstr "5037"') do ( 
	REM set a=%%i
	REM goto killPort
REM )

REM goto :nextLogic

REM :killPort
REM set padid="%a:~71,5%"
REM if not %padid%=="0" taskkill /f /pid %padid%


REM :nextLogic

REM adb kill-server
REM adb start-server
adb devices
adb devices > devices.txt
for /f "skip=1" %%a in (devices.txt) do (
	echo kill %%a
	adb -s %%a shell am force-stop com.hml.dkm 
	::adb -s %%a uninstall com.Company.dkm 
	echo kill %%a
)

taskkill /f /im cmd.exe /t

pause nul
