@echo off


for %%a in ("%Url%") do set "FileName=%%~nxa"

if not defined SavePath set "SavePath=%cd%"

(echo Download Wscript.Arguments^(0^),Wscript.Arguments^(1^)

echo Sub Download^(url,target^)
echo Const adTypeBinary = 1
echo Const adSaveCreateOverWrite = 2
echo Dim http,ado
echo Set http = CreateObject^("Msxml2.ServerXMLHTTP"^)
echo http.open "GET",url,False
echo http.send
echo Set ado = createobject^("Adodb.Stream"^)
echo ado.Type = adTypeBinary
echo ado.Open
echo ado.Write http.responseBody
echo ado.SaveToFile target
echo ado.Close
echo End Sub)>DownloadFile.vbs

echo downloading apk,wait...
DownloadFile.vbs "%Url%" "%SavePath%\%FileName%"
echo downfinish...
del DownloadFile.vbs
