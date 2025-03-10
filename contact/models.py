from django.db import models
from django.utils import timezone

class Contact(models.Model): # Vai ser tipo a tabela
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
