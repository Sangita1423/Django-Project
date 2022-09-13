from django.db import connections
from django.db import models
 

class showemp(models.Model):
    ZONEGRPUNIT = models.CharField(max_length=100)
    class Meta:
        db_table = "sampletable"