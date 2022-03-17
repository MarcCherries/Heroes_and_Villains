from django.db import models



class SuperType(models.Model):
    super_type = models.CharField(max_length=255)