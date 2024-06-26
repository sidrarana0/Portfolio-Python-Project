from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)  # Corrected attribute name
    email = models.EmailField()
    concern = models.TextField()

    def __str__(self):
        return self.name
