#!/usr/bin/env python
# coding:utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

# gerekli sınıfları import ettik

class Program(App):
    def build(self):
        self.x = 0
        self.y = 2

        self.duzen = FloatLayout()
        self.buton = Button(text='Hello world',
                            size_hint=(.2, .1),
                            pos = (self.x,self.y))

        self.duzen.add_widget(self.buton)

        Clock.schedule_interval(self.animasyon,0.1)

        return self.duzen

    def animasyon(self,event = None):
        self.x = self.x + 1

        self.buton.pos = (self.x,self.y)


Program().run()
