from django.db import models
class Inquiry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    organisation = models.CharField(max_length=255, blank=True, null=True)
    service_interested_in = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #Client Deets

    def __str__(self):
        return f"Inquiry from {self.first_name}{self.last_name}({self.email})"
# Create your models here.
