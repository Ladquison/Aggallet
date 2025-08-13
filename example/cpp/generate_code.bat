@echo off

setlocal

set SPEC=%~dp0autogen\spec
set OUTPUT=%~dp0autogen\output

python ..\..\src\armoron.py -s %SPEC% -o %OUTPUT% -c

move %OUTPUT%\*.cpp wasm\src\
move %OUTPUT%\*.h wasm\src\
copy %OUTPUT%\*.d.ts app_angular\src\types\
move %OUTPUT%\*.d.ts app_vite\src\types\
copy %OUTPUT%\WasmCallbackId.ts app_angular\src\types\
move %OUTPUT%\WasmCallbackId.ts app_vite\src\types\
copy %OUTPUT%\WasmWrapper.ts app_angular\src\
move %OUTPUT%\WasmWrapper.ts app_vite\src\

endlocal