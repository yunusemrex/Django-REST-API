from django.db import models

# Create your models here.

class Makale(models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayinlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik