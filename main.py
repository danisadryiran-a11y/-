from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Line, RoundedRectangle
import random

# رنگ پس‌زمینه: سرمه‌ای بسیار تیره
Window.clearcolor = (0.02, 0.02, 0.05, 1)

class NeonButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 1, 1, 1)  # رنگ آبی نئونی
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 15), width=1.5)
            Color(0, 1, 1, 0.05)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[15])

class DiamondApp(App):
    def build(self):
        layout = FloatLayout()

        self.lbl = Label(
            text="[ SYSTEM V6 ONLINE ]\nREADY FOR BUILD",
            font_size='24sp',
            color=(0, 1, 1, 1),
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            bold=True
        )

        btn = NeonButton(
            text="START ENGINE",
            size_hint=(0.6, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.on_start)

        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def on_start(self, instance):
        self.lbl.text = "CONNECTED SECURELY\nVIP ACCESS GRANTED"
        self.lbl.color = (0, 1, 0.5, 1)

if __name__ == "__main__":
    DiamondApp().run()
