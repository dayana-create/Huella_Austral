from django.db import models

class especie (models.Model):
    nombre = models.CharField(max_length=70, unique=True)
    
    class Meta:
        verbose_name_plural ='especies'
        ordering  = ['nombre']
        
    def __str__(self):
        return self.nombre 
        
class ejemplar(models.Model):
    especie = models.ForeignKey (
        especie,
        on_delete= models.PROTECT,
        related_name='ejemplares')
    nombre = models.CharField(max_length=70)
    peso_kg =models.DecimalField(max_digits=8,decimal_places=2)
    fecha_ingreso = models.DateField()
    liberado = models.BooleanField(default = False)
    
    class Meta:
        verbose_name_plural =('ejemplares')
        ordering = ['fecha_ingreso']
    
    def __str__(self):
            return f'{self.nombre} ({self.especie})'



