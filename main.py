# Ashurbanipal
# This application is a multiple platform username/password storage,
# which syncronasa the data through an email client.

# Kivy moduls
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label

# Own moduls for data
import download_data

class AshurbanipalApp(App):

    def build(self):
        return Label(text='Hello world')

# Start the Kivy Application loophole


if __name__ == '__main__':
    AshurbanipalApp().run()
