from django.db import models

# Create your models here.

class todo(models.Model):
    text_var = models.TextField()

    def __str__(self):
        return self.text_var  #Show the actual task to the user from admin  
    