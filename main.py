from kivy.app import App
from kivy.uix.label import Label

class DiamondApp(App):
    def build(self):
        return Label(text="Diamond Ultra 2026\nSystem: Active\nArchitecture: ARM64-v8a")

if __name__ == "__main__":
    DiamondApp().run()
