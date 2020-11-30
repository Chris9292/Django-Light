from django.db import models

# Create your models here.

class Task(models.Model):

    class Meta:
        db_table = "Task"
    
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name