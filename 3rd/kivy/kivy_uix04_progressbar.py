# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

class Program(App):
    def build(self):
        self.bar = ProgressBar(max = 100)
        self.deger = 0

        Clock.schedule_once(self.say,1) # 1 ms sonra self.say adlı fonksiyona git

        return self.bar


    def say(self,event = None):
        if(self.deger <= 100):

            self.bar.value = self.deger
            self.deger += 5

            Clock.schedule_once(self.say,.5)


Program().run()

