from django.db import models

class database(models.Model):
    user_name=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)


