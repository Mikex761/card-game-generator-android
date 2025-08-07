# 📱 Android APK Build Guide

Since you're on Windows and Buildozer requires Linux, here are **3 proven methods** to build your Android APK:

## 🚀 **Method 1: WSL (Windows Subsystem for Linux) - RECOMMENDED**

### **Step 1: Install WSL**
Run in PowerShell as Administrator:
```powershell
wsl --install
wsl --install -d Ubuntu
```
Restart your computer after installation.

### **Step 2: Set up Linux environment**
```bash
wsl
cd /mnt/c/Users/Admin/card_game/android_app/
sudo apt update
sudo apt install -y python3 python3-pip python3-venv build-essential git unzip openjdk-8-jdk
sudo apt install -y autoconf libtool pkg-config zlib1g-dev libncurses5-dev cmake libffi-dev libssl-dev
```

### **Step 3: Install Python dependencies**
```bash
pip3 install --upgrade pip
pip3 install kivy[base]==2.1.0 reportlab pillow pandas openpyxl
pip3 install buildozer==1.4.0 cython==0.29.33
```

### **Step 4: Build the APK**
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
buildozer android debug
```

**Result**: APK file will be in `bin/cardgamegenerator-1.0-armeabi-v7a-debug.apk`

---

## ☁️ **Method 2: GitHub Actions (Cloud Build) - EASIEST**

### **Step 1: Create GitHub Repository**
1. Go to [GitHub.com](https://github.com) and create new repository
2. Upload your `android_app` folder to the repository

### **Step 2: Trigger Build**
1. The GitHub Actions workflow will automatically run
2. Go to "Actions" tab in your repository
3. Download the built APK from "Artifacts"

**Advantages**: 
- No local setup required
- Professional CI/CD pipeline  
- Always works regardless of your OS

---

## 🐳 **Method 3: Docker - FOR ADVANCED USERS**

### **Prerequisites**: Install Docker Desktop

### **Step 1: Run Docker Build**
```batch
build_docker.bat
```

Or manually:
```bash
docker build -t cardgame-builder .
docker run --rm -v ${PWD}:/app cardgame-builder
```

**Result**: APK file will be generated in current directory

---

## 📦 **What You'll Get**

After successful build, you'll have:
- **File**: `cardgamegenerator-1.0-armeabi-v7a-debug.apk`
- **Size**: ~10-20MB (typical for Kivy apps)
- **Compatibility**: Android 5.0+ (API 21+)
- **Architecture**: ARM64 and ARM32 support

## 🧪 **Testing Your APK**

1. **Enable Developer Options** on your Android device
2. **Enable USB Debugging**
3. **Allow Unknown Sources** (for APK installation)
4. **Transfer APK** to your device via:
   - USB cable
   - Email attachment
   - Cloud storage (Google Drive, Dropbox)
   - ADB install: `adb install cardgamegenerator-1.0-armeabi-v7a-debug.apk`

## ⚠️ **Troubleshooting**

### **Common Issues:**

1. **"Buildozer command not found"**
   - Solution: Reinstall buildozer in Linux environment

2. **"Java not found"**  
   - Solution: Set `JAVA_HOME` correctly

3. **"NDK/SDK errors"**
   - Solution: Let buildozer download automatically (first run takes longer)

4. **"Permission denied"**
   - Solution: Run with proper permissions in Linux/WSL

### **Build Time Expectations:**
- **First build**: 20-60 minutes (downloads NDK, SDK, dependencies)
- **Subsequent builds**: 2-10 minutes
- **File size**: 15-25MB final APK

## 🎯 **Recommended Approach**

1. **Start with Method 2 (GitHub Actions)** - easiest and most reliable
2. **Use Method 1 (WSL)** if you want local builds  
3. **Method 3 (Docker)** only if you're familiar with containerization

## 🔧 **Build Configuration**

Your app is configured with:
- **Package**: com.cardgame.generator
- **Version**: 1.0
- **Target API**: Android 13 (API 33)
- **Min API**: Android 5.0 (API 21)
- **Permissions**: Storage access for image uploads and PDF generation

## 📱 **App Features in APK**

Your APK will include all features:
- ✅ Mobile UI with forms and buttons
- ✅ Image upload and processing (20mm × 20mm)
- ✅ 8 different card suits + 6 colors
- ✅ PDF generation (26mm × 36.4mm cards)
- ✅ POS printer optimization (30mm paper)
- ✅ Professional card layout and design

---

**🚀 Ready to build your APK? Choose your preferred method and follow the steps above!**
