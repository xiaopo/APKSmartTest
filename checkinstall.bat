@echo off

title  %1   %packName%


echo %1 Installing APK %2
set packagex=package:%packName%
for /f "tokens=*" %%i in ('adb -s %1 shell pm list package') do (
	if %%i == %packagex% (
		echo areadly install apk %packName%
		goto :install_success
		break
	)
)

::°²×°
adb -s %1 install -r %2

:install_success

start adb_commd %1 %apkpath% 


exit
 
