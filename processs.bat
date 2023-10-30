@echo off
setlocal enabledelayedexpansion

rem Get the input and output folder paths from command-line arguments
set "input_folder=%~1"
set "output_folder=%~2"

rem Verify that the input folder exists
if not exist "%input_folder%\" (
    echo Input folder not found.
    exit /b 1
)

rem Verify that the output folder exists or create it if not
if not exist "%output_folder%\" (
    mkdir "%output_folder%"
)

rem Process each .msg and .eml file in the input folder
for %%I in ("%input_folder%\*.msg" "%input_folder%\*.eml") do (
    if exist "%%~I" (
        rem Run the Python script and capture its output to a file
        set "response_file=%output_folder%\%%~nI.response.txt"
        "C:\Program Files\Python311\python.exe" "C:\Users\hp\Desktop\sem 2 mini project\Kanishk MIni Project\kanishkminiproject.py" "%%~I" > "!response_file!" 2>&1
        echo Processed %%~I and saved response as !response_file!
    )
)

echo Processing complete.
