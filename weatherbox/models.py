from django.db import models

# Create your models here.


class Data(models.Model):

    class Meta:
        db_table = "sensor_data"

    s_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=20)
    value = models.FloatField()
    measurement_unit = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"id: {self.id}\ns_id: {self.s_id}\nname: {self.name}\n" \
               f"value: {self.value}\nmeasurement_unit: {self.measurement_unit}\ndate: {self.date}\n"
