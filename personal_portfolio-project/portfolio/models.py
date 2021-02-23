from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
