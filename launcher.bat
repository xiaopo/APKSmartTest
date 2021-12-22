@echo off


set SavePath=%cd%

::set Url="http://10.0.1.127/duokemeng_1.0.2.2_20200409/Android/out.apk"
set Url="http://10.0.1.73/game/mailiang/release/NW-Android-10211.apk"


set forceDownload=false
set apkpath=%SavePath%\NW-Android-10211.apk


REM set packName=com.Company.dkm
REM set mainActivity=com.unity3d.player.UnityPlayerActivity

set packName=com.hml.dkm
set mainActivity=com.hml.sdk.HmlDkmMainActivity

set dllpath=%SavePath%\exe\GameProfiler.dll
set luapath=%SavePath%\lua\GameProfiler.lua
set outDataPath=%SavePath%\output


set basefloder=/sdcard/Android/data/%packName%/files
set folder=%basefloder%/GameProfiler/



if exist %apkpath% (
	if %forceDownload%==true (
		call download
		
	) else ( echo use local apk %apkpath%	)

) else (

	call download
)


REM for /f "delims=  tokens=1" %%i in ('netstat -aon ^| findstr "5037"') do ( 
	REM set a=%%i
	REM goto killPort
REM )

REM goto :nextLogic

REM :killPort
REM set 
REM set padid="%a:~71,5%"
REM if not %padid%=="0" taskkill /f /pid %padid%


REM :nextLogic
adb kill-server
adb start-server
adb devices
adb devices > devices.txt


for /f "skip=1" %%a in (devices.txt) do ( 
	start checkinstall %%a %apkpath% 
	echo .
)



REM goto :start_analysis_data

REM :::::::::::::::::::::analysis files ::::::::::::::::::::::::::::
REM set exe1=%SavePath%\exe\GameProfilerLoad.exe
REM set exe2=%SavePath%\exe\CSVToJson.exe

REM :start_analysis_data
REM echo ---------------------------------------------------------------

REM ::pull file 
REM REM for /f "skip=1" %%b in (devices.txt) do ( 
	REM REM echo start pull file  %%b
	REM REM set outPath=%outDataPath%\%%a\
	REM REM set devName=%%a
	REM REM ::goto pull_file
REM REM )


REM ::convert data
REM echo start convert data to csv
REM set outDir=%SavePath%\output
REM for /R %outDir% %%f in (*.data) do ( 
	REM exe1 %%f 
REM )

REM goto :start_analysis_data

REM :pull_file
REM if exist %outPath% (
	REM echo ....................
REM ) else (
	REM md %outPath%
REM )
REM ::pul pul
REM ::adb -s %devName% pull %folder%profile.data %outPath% 

