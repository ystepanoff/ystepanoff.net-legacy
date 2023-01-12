from django.db import models


class Project(models.Model):
    identifier = models.TextField()
    title = models.TextField()
    image = models.TextField()
    description = models.TextField()
    url = models.TextField()
    content = models.TextField()

