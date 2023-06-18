from django.db import models

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    number = models.TextField()
