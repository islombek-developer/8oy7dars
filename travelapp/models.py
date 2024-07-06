
from django.db import models

class Sayohat_turi(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Travel(models.Model):
    sayohat_turi = models.ForeignKey(Sayohat_turi, on_delete=models.CASCADE)
    aviakompaniya = models.CharField(max_length=100)
    davomiyligi = models.IntegerField()
    ovqatlanish = models.CharField(max_length=100)
    viza = models.BooleanField()
    bonuslar = models.TextField()

    def __str__(self):
        return self.aviakompaniya
    
    
