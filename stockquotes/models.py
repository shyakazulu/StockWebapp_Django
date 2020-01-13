from django.db import models

class dbstock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker