from django.db import models

class datos_copeinca(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    caldero_1=models.BooleanField()
    caldero_2=models.BooleanField()
    caldero_3=models.BooleanField()
    caldero_4=models.BooleanField()
    caldero_5=models.BooleanField()
    caldero_6=models.BooleanField()
    caldero_7=models.BooleanField()
    caldero_8=models.BooleanField()
    energia=models.FloatField()
    velocidad=models.FloatField()
    liquido=models.FloatField()

    def __str__(self):
        return self.fecha + '-' + self.hora + '-' + self.caldero_1 + '-' + self.caldero_2 + '-' + self.caldero_3 + '-' + self.caldero_4 + '-' + self.caldero_5 + '-' + self.caldero_6 + '-' + self.caldero_7 + '-' + self.caldero_8 + '-' + self.energia + '-' + self.velocidad + '-' + self.liquido
