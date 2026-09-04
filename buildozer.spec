[app]
title = Banking Exam Prep
package.name = bankingexamprep
package.domain = com.subhamoy
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt
version = 1.0.0
requirements = python3==3.11.8,hostpython3==3.11.8,kivy==2.3.1
orientation = portrait
fullscreen = 0

# Android
android.api = 36
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True
android.uses_cleartext = False

# App icon


[buildozer]
log_level = 2
warn_on_root = 1
