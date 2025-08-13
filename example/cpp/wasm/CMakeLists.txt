cmake_minimum_required(VERSION 3.31)
project(WasmProject)

set(TARGET_NAME "WASM")
set(APP_ANGULAR_PATH "${CMAKE_SOURCE_DIR}/../app_angular")
set(APP_VITE_PATH "${CMAKE_SOURCE_DIR}/../app_vite")
set(THIRD_PATH "${CMAKE_SOURCE_DIR}/../3rd")
set(EMSDK_PATH "${THIRD_PATH}/emsdk")

file(GLOB SRC_FILES
	"${CMAKE_SOURCE_DIR}/src/*.cpp"
	"${CMAKE_SOURCE_DIR}/src/*.h"
)

add_executable(${TARGET_NAME} ${SRC_FILES})

target_include_directories(${TARGET_NAME} PRIVATE
	"${EMSDK_PATH}/upstream/emscripten/cache/sysroot/include"
)

target_compile_options(${TARGET_NAME} PRIVATE
	"-gsource-map" # this option is required to debug
	"-O0" # this option is required to debug
)

target_link_options(${TARGET_NAME} PRIVATE
	"-gsource-map" # this option is required to debug
	"-O0" # this option is required to debug
	"--bind"
	"-sMODULARIZE=1"
	"-sEXPORT_ES6=1"
	"-sEXPORT_NAME=${TARGET_NAME}"
	"-sENVIRONMENT='web'"
	"-sALLOW_MEMORY_GROWTH=1"
	"--no-entry"
)

set_target_properties(${TARGET_NAME} PROPERTIES SUFFIX ".js")

install(FILES
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.js"
	DESTINATION "${APP_ANGULAR_PATH}/src/wasm"
)
install(FILES
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.js"
	DESTINATION "${APP_VITE_PATH}/src/wasm"
)
install(FILES
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.wasm"
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.wasm.map"
	DESTINATION "${APP_ANGULAR_PATH}/public/wasm"
)
install(FILES
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.wasm"
	"${CMAKE_BINARY_DIR}/${TARGET_NAME}.wasm.map"
	DESTINATION "${APP_VITE_PATH}/public/wasm"
)
