[app]
# App basic info
title = Card Game Generator
package.name = cardgamegenerator
package.domain = com.cardgame.generator

# App source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# App version
version = 1.0

# App requirements
requirements = python3,kivy,reportlab,pillow,pandas,openpyxl

# App main module
source.main = main.py

# App icon and presplash
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# App orientation
orientation = portrait

# App services
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

[buildozer]
# Build directory
log_level = 2
warn_on_root = 1

# Android specific
[android]
# NDK and SDK paths
#android.ndk_path =
#android.sdk_path =

# Android API and NDK versions
android.api = 33
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21

# Android architecture
android.archs = arm64-v8a, armeabi-v7a

# Android permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET,ACCESS_NETWORK_STATE

# Android app theme
android.theme = "@android:style/Theme.NoTitleBar"

# Android gradle dependencies
android.gradle_dependencies = 

# Android add source files
#android.add_src = 

# Android add activity to manifest
#android.add_activity = com.example.ExampleActivity

# Android add Java files
#android.add_java_dir =

# Android add resource directories
#android.add_res_dir =

# Android manifest entries
android.manifest.intent_filters = 

# Android signing
#android.debug.keystore = ~/.android/debug.keystore

# iOS specific
[ios]
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0
