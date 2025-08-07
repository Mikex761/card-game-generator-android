#!/usr/bin/env python3
"""
Setup script for Android Card Game Generator App
This script helps set up the development environment and build the Android app.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description=""):
    """Run a command and print its output"""
    print(f"\n{'='*60}")
    print(f"Running: {description if description else command}")
    print('='*60)
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=False, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with return code {e.returncode}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("Warning: Python 3.8+ is recommended for Kivy development")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\nInstalling Python dependencies...")
    
    dependencies = [
        "pip install --upgrade pip",
        "pip install kivy[base]>=2.1.0",
        "pip install reportlab>=3.6.0", 
        "pip install Pillow>=9.0.0",
        "pip install pandas>=1.3.0",
        "pip install openpyxl>=3.0.0"
    ]
    
    for dep in dependencies:
        if not run_command(dep, f"Installing: {dep.split()[-1]}"):
            print(f"Failed to install {dep}")
            return False
    
    return True

def test_app():
    """Test the app locally before building for Android"""
    print("\nTesting app locally...")
    return run_command("python main.py", "Testing Card Game Generator App")

def setup_buildozer():
    """Set up Buildozer for Android compilation"""
    print("\nSetting up Buildozer for Android...")
    
    if platform.system() == "Windows":
        print("Note: Buildozer works best on Linux. For Windows, consider:")
        print("1. Using WSL (Windows Subsystem for Linux)")
        print("2. Using a Linux virtual machine")
        print("3. Using online build services")
        return False
    
    commands = [
        "pip install buildozer",
        "pip install cython"
    ]
    
    for cmd in commands:
        if not run_command(cmd):
            return False
    
    return True

def build_android_debug():
    """Build Android debug APK"""
    print("\nBuilding Android debug APK...")
    
    if not os.path.exists("buildozer.spec"):
        print("Error: buildozer.spec not found!")
        return False
    
    return run_command("buildozer android debug", "Building Android APK")

def main():
    """Main setup function"""
    print("Card Game Generator - Android App Setup")
    print("="*60)
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    if not install_dependencies():
        print("Failed to install dependencies")
        return 1
    
    print("\n" + "="*60)
    print("Setup completed!")
    print("="*60)
    
    print("\nNext steps:")
    print("1. Test the app: python main.py")
    print("2. For Android build on Linux: python setup_android.py --build")
    print("3. For Windows users: Consider using WSL or Linux VM")
    
    # Check if user wants to test the app
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_app()
    elif len(sys.argv) > 1 and sys.argv[1] == "--build":
        if setup_buildozer():
            build_android_debug()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
