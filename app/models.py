from django.db import models

# Create your models here.


class Song(models.Model):
    Sname=models.CharField(max_length=100)
    Ssinger=models.CharField(max_length=100)
    Smusicdirector=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname
