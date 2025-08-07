@echo off
echo ================================================
echo Card Game Generator - Docker APK Builder
echo ================================================
echo.

echo This script will build the Android APK using Docker
echo Make sure Docker Desktop is installed and running!
echo.

echo Step 1: Building Docker image...
echo --------------------------------
docker build -t cardgame-builder .

echo.
echo Step 2: Running Docker container to build APK...
echo ----------------------------------------------
docker run --rm -v %cd%:/app cardgame-builder

echo.
echo Step 3: Copying APK from container...
echo -----------------------------------
docker run --rm -v %cd%:/host cardgame-builder cp /app/bin/*.apk /host/

echo.
echo Done! Check for APK file in the current directory.
echo.
pause
