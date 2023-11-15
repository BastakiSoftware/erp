from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.

class Model(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    last_update_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})


    

    
