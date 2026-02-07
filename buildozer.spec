[app]
title = Diamond Ultra Pro
package.name = diamondultra
package.domain = org.iran.a11y
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.0.0
requirements = python3,kivy

# تنظیمات گرافیکی (آیکون غیرفعال شد تا ارور ندهد)
# icon.filename = icon.png
orientation = portrait
fullscreen = 1

# تنظیمات فنی اندروید
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.permissions = INTERNET
