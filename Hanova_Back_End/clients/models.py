from django.db import models
class clients(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
#the name of you venv is myvenv tsk and this is how you activate it myenv\Scripts\activate