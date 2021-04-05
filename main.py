# Ashurbanipal
# This application is a multiple platform username/password storage,
# which syncronasa the data through an email client.

# Kivy moduls
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Own moduls for data
import download_data
import en_decrypt_data
import importdata

class AshurbanipalApp(App):

    def build(self):

        # Basic frame
        root_widget = BoxLayout(orientation='horizontal')

        return root_widget

# Start the Kivy Application loophole


if __name__ == '__main__':
    AshurbanipalApp().run()
