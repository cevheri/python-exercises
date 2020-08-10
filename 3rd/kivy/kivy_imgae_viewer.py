# -*- coding: utf-8 -*-
# Image viewer

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
import os

class Program(App):

    def resimYukle(self,dosya_yolu):
        # Format listesi
        liste = ["png","gif","jpeg","jpg"]

        # Dosyaların listesini alma
        dosyaListesi = os.listdir(dosya_yolu)
        self.sayac = 0
        self.bar.max = len(dosyaListesi)
        self.bar.value = 0

        # Resim dosyalarını tespit etme
        for i in dosyaListesi:
            if(i.split(".")[-1] in liste):
                self.resimListesi.append(i)

            self.sayac += 1
            self.bar.value = self.sayac

        # Resimlerin yüklenmesi bittikten sonra, görüntüleme ekranını başlatmak üzere
        # self.basla fonksiyonuna git
        self.yukleniyor.text = "Resimler yüklendi"
        Clock.schedule_once(self.basla,1.5)

    def build(self):
        self.resimYolu = "/home/cevher/Pictures/"
        self.resimListesi = list()
        self.resimSirasi = 0

        self.yukleniyor = Label(text = "Resimler yükleniyor...")
        self.bar = ProgressBar()

        self.govde = BoxLayout(orientation = "vertical")
        self.govde.add_widget(self.yukleniyor)
        self.govde.add_widget(self.bar)

        # Resimleri yüklemek üzere, self.resimYukle fonksiyonuna git
        Clock.schedule_once(lambda event = None:self.resimYukle(self.resimYolu),1)

        return self.govde

    def basla(self,event = None):
        # Ekrandaki tüm araçları kaldırıyoruz
        self.govde.clear_widgets()

        # Ve yeni araçlarımızı ekliyoruz
        self.bilgi = Label(text = "Resim Görüntüleyici",
                               markup = True,
                               size_hint_y = .1)
        self.resim = Image(source = self.resimYolu+self.resimListesi[0],
                           allow_stretch = True,
                           keep_ratio = True)


        # Geri ve ileri butonlarını taşıyan BoxLayout
        self.butonBar = BoxLayout(size_hint_y = .15)

        self.ileri = Button(text = "ileri",
                            size_hint_x = .2,
                            on_release = self.ileriYukle
                            )

        self.geri = Button(text = "geri",
                           size_hint_x = .2,
                           on_release = self.geriYukle)

        self.butonBar.add_widget(self.geri)
        self.butonBar.add_widget(Widget())
        self.butonBar.add_widget(self.ileri)

        self.govde.add_widget(self.bilgi)
        self.govde.add_widget(self.resim)
        self.govde.add_widget(self.butonBar)


    def ileriYukle(self,event = None):
        self.resimSirasi += 1

        # Eğer resim sırası listemizin boyutunu aşmamışsa
        if(self.resimSirasi < len(self.resimListesi)):
            try:
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer liste boyutunu aşmışsa, bunu sıfırlıyoruz
        else:
            try:
                self.resimSirasi = 0
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]

            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])


    def geriYukle(self,event = None):
        self.resimSirasi -= 1

        # Eğer resim sırası listemizin boyutunun altına düşmemişse
        if(self.resimSirasi >= 0):
            try:
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer düşmüşse, yani negatif olduysa
        # sırayı listenin sonuna alıyoruz
        else:
            try:
                self.resimSirasi = len(self.resimListesi)-1
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

Program().run()
