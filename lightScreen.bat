@echo off

adb devices
adb devices > devices.txt
for /f "skip=1" %%a in (devices.txt) do (
	echo light %%a
	adb -s %%a shell input keyevent 82
	adb -s %%a shell svc power stayon true 
)


pause nul
