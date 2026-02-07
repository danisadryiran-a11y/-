from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# تنظیم رنگ پس‌زمینه (تیره)
Window.clearcolor = (0.02, 0.02, 0.05, 1)

class DiamondApp(App):
    def build(self):
        layout = FloatLayout()

        # متن خوش‌آمدگویی
        label = Label(
            text="DIAMOND ULTRA\n[ SYSTEM ACTIVE ]",
            font_size='32sp',
            halign='center',
            color=(0, 0.7, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        # دکمه شروع
        btn = Button(
            text="START ENGINE",
            size_hint=(0.6, 0.12),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0, 0.5, 0.8, 1),
            font_size='20sp'
        )

        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    DiamondApp().run()
