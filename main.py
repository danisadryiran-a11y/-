from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# بهینه‌سازی برای نمایشگرهای موبایل
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class DiamondApp(App):
    def build(self):
        self.title = "Diamond Ultra"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.lbl = Label(
            text="DIAMOND READY\nSecure Tunneling", 
            font_size='22sp', 
            halign='center',
            color=(0, 0.7, 1, 1)
        )
        
        btn = Button(
            text="CONNECT",
            size_hint=(1, 0.3),
            background_normal='',
            background_color=(0.1, 0.5, 0.8, 1),
            font_size='20sp'
        )
        btn.bind(on_press=self.start)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def start(self, instance):
        self.lbl.text = "Status: ACTIVE\n[Encrypted Mode]"
        self.lbl.color = (0.2, 1, 0.5, 1)

if __name__ == "__main__":
    DiamondApp().run()

