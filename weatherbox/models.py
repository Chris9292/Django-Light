from django.db import models

# Create your models here.


class Data(models.Model):

    class Meta:
        db_table = "sensor_data"

    name = models.CharField(max_length=20)
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"\nid : {self.id}, value: {self.value}\n"

