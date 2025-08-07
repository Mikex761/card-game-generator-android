@echo off
echo ================================================
echo Card Game Generator - Android APK Builder
echo ================================================
echo.
echo This script will help you build the Android APK using WSL
echo.

echo Step 1: Install WSL (if not already installed)
echo -------------------------------------------
echo Run these commands in PowerShell as Administrator:
echo.
echo    wsl --install
echo    wsl --install -d Ubuntu
echo.
echo Then restart your computer and continue to Step 2.
echo.

echo Step 2: Copy files to WSL
echo -------------------------
echo After WSL is installed, run these commands:
echo.
echo    wsl
echo    cd /mnt/c/Users/Admin/card_game/android_app/
echo    sudo apt update
echo    sudo apt install -y python3 python3-pip python3-venv
echo    sudo apt install -y build-essential git unzip
echo    sudo apt install -y openjdk-8-jdk
echo.

echo Step 3: Install Python dependencies
echo -----------------------------------
echo    pip3 install kivy[base] reportlab pillow buildozer cython
echo    pip3 install pandas openpyxl
echo.

echo Step 4: Build the APK
echo ---------------------
echo    buildozer android debug
echo.

echo The APK file will be created in the 'bin' directory
echo File will be named: cardgamegenerator-1.0-armeabi-v7a-debug.apk
echo.

pause
