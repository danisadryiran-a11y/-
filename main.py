from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Line, RoundedRectangle
from kivy.animation import Animation
import random

# تنظیم رنگ پس‌زمینه به رنگ "مشکی عمیق"
Window.clearcolor = (0.05, 0.05, 0.08, 1)

class CyberButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # حذف پس‌زمینه پیش‌فرض
        self.background_normal = ''
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # ایجاد کادر نئونی دور دکمه
            Color(0, 1, 0.8, 1)  # رنگ فیروزه‌ای نئونی
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 10), width=1.5)
            Color(0, 1, 0.8, 0.1) # هاله نورانی داخل دکمه
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

class DiamondProApp(App):
    def build(self):
        layout = FloatLayout()

        # تیتر اصلی با افکت سایه
        self.status_label = Label(
            text="[ DIAMOND SYSTEM V5.0 ]\nWAITING FOR COMMAND...",
            font_size='26sp',
            halign='center',
            color=(0, 1, 0.8, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            bold=True
        )

        # دکمه حرفه‌ای
        self.btn = CyberButton(
            text="INITIATE CONNECTION",
            size_hint=(0.7, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_size='18sp',
            color=(0, 1, 0.8, 1)
        )
        self.btn.bind(on_press=self.animate_action)

        # متن فوتر (پایین صفحه)
        footer = Label(
            text="SECURE ENCRYPTED CONNECTION",
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )

        layout.add_widget(self.status_label)
        layout.add_widget(self.btn)
        layout.add_widget(footer)
        return layout

    def animate_action(self, instance):
        # شبیه‌سازی اتصال به سرور
        self.status_label.text = "CONNECTING TO SERVER..."
        self.status_label.color = (1, 0, 0.5, 1) # تغییر رنگ به صورتی
        
        # انیمیشن بزرگ و کوچک شدن دکمه
        anim = Animation(size_hint=(0.65, 0.09), duration=0.1) + Animation(size_hint=(0.7, 0.1), duration=0.1)
        anim.start(instance)
        
        # تغییر متن بعد از ۲ ثانیه (شبیه‌سازی)
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.success_connect(), 2)

    def success_connect(self):
        ip = f"192.168.{random.randint(1,99)}.{random.randint(1,99)}"
        self.status_label.text = f"[ SYSTEM CONNECTED ]\nIP: {ip}"
        self.status_label.color = (0, 1, 0, 1) # سبز

if __name__ == "__main__":
    DiamondProApp().run()
