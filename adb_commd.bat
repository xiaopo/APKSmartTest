@echo off

title  %1   %packName%


::�ر�
adb -s %1 shell am force-stop %packName%
::����
adb -s %1 shell input keyevent 82
::��Ļ����
REM adb -s %1 shell svc power stayon true 
REM ::Ȩ����Ȩ
REM adb -s %1 -d shell pm grant %packName% android.permission.RECORD_AUDIO
REM adb -s %1 -d shell pm grant %packName% android.permission.WRITE_EXTERNAL_STORAGE
REM adb -s %1 -d shell pm grant %packName% android.permission.READ_EXTERNAL_STORAGE



echo #############################Run Game %packName% 
::������Ϸ
for /f %%i in ('adb -s %1 shell am start -n  %packName%/%mainActivity%') do (

	if "%%i" == "Starting:" ( 
		goto :run_game_scecess 
	) else ( 
		goto :run_game_fail 
	)
)


:run_game_fail
 echo run game faild plaese check your devices
 goto :end_end
 
 
:run_game_scecess

choice /t 2 /d y /n >nul

::�����ļ�

echo #############################push files %1  GameProfiler.dll GameProfiler.lua


adb -s %1 shell mkdir %basefloder%
adb -s %1 shell mkdir %folder% 

adb -s %1 push %dllpath% %folder%
adb -s %1 push %luapath% %folder%

::�ӳ�����




::����airTestIDE
start airtest 127.0.0.1:5037/%1 %1

::���ݽ���
start analysis %1

:end_end
exit

