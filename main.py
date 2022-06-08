import aprs
from kivy.uix.label import Label
from kivy.app import App
from plyer import gps


class YourApp(App):

    def build(self):
        root_widget = Label(text='Hello world!')
        return root_widget


if __name__ == '__main__':
    YourApp().run()
