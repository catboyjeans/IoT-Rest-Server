from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    state1 = models.DecimalField(max_digits=10, decimal_places=4)
    state2 = models.DecimalField(max_digits=10, decimal_places=4)
    state3 = models.DecimalField(max_digits=10, decimal_places=4)
    state4 = models.DecimalField(max_digits=10, decimal_places=4)
    state5 = models.DecimalField(max_digits=10, decimal_places=4)
    state6 = models.DecimalField(max_digits=10, decimal_places=4)
    state7 = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.first_name
    