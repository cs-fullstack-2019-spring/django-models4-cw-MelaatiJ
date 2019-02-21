from django.db import models

# Create your models here.

#moms model that shows her name so i can remember which child to connect it to

class Mom(models.Model):
    mom_first_name = models.CharField(max_length=100)
    mom_last_name = models.CharField(max_length=100)
    mom_phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.mom_first_name}{self.mom_last_name}'
#child model that has a foreignkey which leads to the choices of moms
class Child(models.Model):
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_mom = models.ForeignKey(Mom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.child_first_name} {self.child_last_name}'

