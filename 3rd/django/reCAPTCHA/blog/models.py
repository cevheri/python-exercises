from django.db import models


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, verbose_name='Kullanıcı Adınız')
    comment = models.TextField(verbose_name='Yorumunuz')
