# Ashurbanipal
# This application is a multiple platform username/password storage,
# which syncronasa the data through an email client.

# Kivy moduls
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label

# Own modul for data


class AshurbanipalApp(App):

    def build(self):
        return Label(text='Hello world')

# Start the Kivy Application loophole


if __name__ == '__main__':
    AshurbanipalApp().run()
