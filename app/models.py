from django.contrib.auth.models import User
from django.db import models
from root.models import BaseModel

# Create your models here.

class Company(BaseModel):
    name = models.CharField(max_length=256,unique=True)
    phone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Declaration(BaseModel):
    class Status(models.TextChoices):
        FINISHED = "F", "Finished"
        IN_PROCESS = "I", "In process"

    
    class Modes(models.TextChoices):
        IM70 = "IM70", "IM 70"
        IM40 = "IM40", "IM 40"
        ND40 = "ND40", "ND 40"

    declarant = models.ForeignKey(User,on_delete=models.CASCADE)
    number_gtd = models.CharField(max_length=256)
    reference_gtd = models.CharField(max_length=256)
    date_recorded = models.CharField(max_length=256)
    customs_mode = models.CharField(max_length=10,choices=Modes.choices)
    sender = models.ManyToManyField(Company,related_name="senders")
    reciever = models.ManyToManyField(Company,related_name="recievers")
    country = models.CharField(max_length=256)
    custom_price = models.DecimalField(max_digits=10,decimal_places=2)
    factor_price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=1,choices=Status.choices)

    def __str__(self) -> str:
        return f"{self.declarant.first_name} {self.declarant.last_name}'s declaration"
