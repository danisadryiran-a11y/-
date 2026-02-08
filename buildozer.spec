[app]
title = Diamond Ultra V6
package.name = diamond.fix
package.domain = com.v6.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 6.0.0

# الزامات اصلی (ساده شده برای جلوگیری از خطا)
requirements = python3,kivy==2.2.1,kivymd,pillow

# آیکون فعلا غیرفعال (برای اطمینان از ساخت فایل)
# icon.filename = icon.png

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
p4a.branch = master
