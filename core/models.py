from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)
    content = models.FileField(upload_to='contents')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

