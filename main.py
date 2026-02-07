from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.02, 0.02, 1)

class DiamondApp(App):
    def build(self):
        self.title = "Diamond Ultra v8"
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        self.status_label = Label(text="DIAMOND STEALTH\n[Ready]", font_size='24sp', halign='center', color=(0, 0.9, 1, 1))
        connect_btn = Button(text="START CONNECTION", size_hint=(1, 0.4), background_color=(0.1, 0.6, 0.2, 1), font_size='20sp')
        connect_btn.bind(on_press=self.on_connect)
        layout.add_widget(self.status_label)
        layout.add_widget(connect_btn)
        return layout

    def on_connect(self, instance):
        self.status_label.text = "Status: CONNECTED\n(Nano-Fragment Active)"
        self.status_label.color = (0.2, 1, 0.2, 1)

if __name__ == "__main__":
    DiamondApp().run()
