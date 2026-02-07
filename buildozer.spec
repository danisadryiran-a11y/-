[app]
# مشخصات برنامه
title = Diamond Ultra V5
package.name = diamond.pro.max
package.domain = com.master.code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.0.0

# نیازمندی‌های سیستمی
requirements = python3,kivy,pillow

# تنظیمات آیکون و اسپلش
icon.filename = icon.png
orientation = portrait
fullscreen = 0 
# (صفر گذاشتیم تا نوار وضعیت گوشی دیده شود، حرفه‌ای‌تر است)

# تنظیمات اندروید
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 34
android.minapi = 21

# دسترسی‌ها
android.permissions = INTERNET, ACCESS_NETWORK_STATE
