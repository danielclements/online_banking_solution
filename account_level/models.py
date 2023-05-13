from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=120)
    dob = models.DateField()
    plus_member = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=9)
    street_name = models.CharField(max_length=128)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    postcode = models.IntegerField(max_length=5)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Province(models.Model):
    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name