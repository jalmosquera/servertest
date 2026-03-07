from django.db import models




class Pruebas(models.Model):
    name = models.CharField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"
        ordering = ["name"]
    
