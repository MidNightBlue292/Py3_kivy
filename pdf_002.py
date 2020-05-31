"""

Window 'Hello World'

"""

import kivy

kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from pyglet import clock

class MyApp(App):

    def build(self):
        return Label(text='Hello world')


def animate_something():
    from time import sleep
    while True:
        sleep(.10)
    return

def my_callback(dt):
    print('My callback is called', dt)
    return


if __name__ == '__main__':
    
    #animate_something()  # Crash test 1
    event = clock.schedule_interval(my_callback, 1 / 30.)    
    MyApp().run()
