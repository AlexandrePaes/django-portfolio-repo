from django.db import models

class Project(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='alexandrepaes_portfolio_app/images/')
    url = models.URLField(blank=True)
