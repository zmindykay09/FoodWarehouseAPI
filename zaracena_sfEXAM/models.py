from django.db import models

# Create your models here.

class foodstuff(models.Model):
    Mfd_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=60)
    UnitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    UnitsInStock = models.PositiveSmallIntegerField()

    def _str_(self):
        return self.Name