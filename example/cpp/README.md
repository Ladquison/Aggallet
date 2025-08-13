# Overview

This sample demonstrates how to build WebAssembly from C++ and integrate it into web applications.  
Currently, only Windows is supported.

You can run the sample as-is, but if you wish to modify the code, please follow the steps below.

---

# Build Environment

To compile C++ source code into WebAssembly, set up the following tools:
 - Visual Studio Code
 - [CMake](https://cmake.org/download/) (3.31 or higher)
 - [Emscripten SDK](https://github.com/emscripten-core/emsdk)
 - [Ninja](https://github.com/ninja-build/ninja/releases)

Place the Emscripten SDK in the `3rd/emsdk` directory.  
For Ninja, simply place `ninja.exe` in `3rd/ninja`.

Then run `wasm/setup.bat` to initialize the build environment using CMake.

---

# Define Function Specification

To define the functions exposed to WebAssembly, edit the following files:

- `autogen/spec/api.yaml`  
- `autogen/spec/callback.yaml`

After editing, run `generate_code.bat` to generate the corresponding C++ code.

---

# Update C++ code

Open the `cpp/wasm` folder in Visual Studio Code and implement your business logic.  
The generated code will call methods in the `AppWrapper` class by name, but you must provide the actual implementation.

Once editing is complete, press `Ctrl + Shift + B` to build the project.  
The resulting `.js`, `.wasm` and `.map` files will be copied to the appropriate web app folder.

---


# Update Web App code

Sample integrations are provided for both Angular and Vite.  
In both cases, the default callback function registered in WebAssembly will log messages to the console.

## Angular

Navigate to the `app_angular` folder and run:
```
npm install
```
Edit `src/app/app.component.ts` to call your WebAssembly functions.  
Then start the server:
```
ng serve
```
Access the app via your browser.

## Vite

Navigate to the `app_vite` folder and run:
```
npm install
```
Edit src/main.ts to call your WebAssembly functions.  
Then start the server:
```
npm run dev
```
Access the app via your browser.

---

# Debug C++ with Visual Studio Code

This section explains how to debug C++ code using Visual Studio Code.  
Note: Debugging has only been verified with the Chrome browser.

1. Launch Chrome with remote debugging enabled.
Ensure the port matches the one specified in `launch.json`.
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%TEMP%\chrome-wasm-debug"
```

2. Start either the Angular or Vite server.

3. In Visual Studio Code, run the appropriate debug configuration:
   - Attach to Chrome (Angular)
   - Attach to Chrome (Vite)

4. Set breakpoints in your C++ code, interact with the app in your browser, and observe the breakpoints being hit.