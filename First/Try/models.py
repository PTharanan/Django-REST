from django.db import models

class Sample(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    