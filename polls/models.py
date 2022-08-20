from django.db import models

# Create your models here.
class inviteMarried_request(models.Model)    :
    maleName=models.CharField(max_length=200)
    femaleName=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    clock=models.CharField(max_length=200)
    date=models.DateField()