@echo off
setlocal

set EMSDK_PATH="..\3rd\emsdk"

call %EMSDK_PATH%"\emsdk_env.bat"
mkdir build
cd build
cmake -S .. --preset=default
cmake --build .
cmake --install .

endlocal