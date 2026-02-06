[app]
title = Diamond Ultra
package.name = sh.diamond.ultra
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 8.5.0

# پیش‌نیازهای سیستمی
requirements = python3,kivy,hostpython3,requests

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE

# پشتیبانی از پردازنده‌های جدید (Xiaomi 11/12/13/14) و گوشی‌های قدیمی
android.archs = arm64-v8a, armeabi-v7a

# هماهنگی با اندروید 11 تا 14
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
