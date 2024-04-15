from django.db import models

# Create your models here.
class AutorDb(models.Model):
    
    nombre = models.CharField(max_length=50,
                            verbose_name= "Nombre")
    fecha_de_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento",
                                           null=False,
                                           blank=False)
    fecha_de_fallecimiento = models.DateField(verbose_name="Fecha de Fallecimiento",
                                              null=True, blank=True)
    profesion = models.CharField(max_length=50,
                               verbose_name="Profesión",)
    nacionalidad=models.CharField(max_length=50,
                                  verbose_name="Nacionalidad",)
    
    class Meta:
        db_table = 'AutorDb'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self) -> str:
        return self.nombre
    
class FraseDb(models.Model):
    cita = models.TextField(max_length=1000,
                          verbose_name="cita",
                          )
    #se crea el campo buscando el argumento de la tabla del autor Db con ForeignKey y
    #un many2one, y se parametriza un (on_delete=modelo.CASCADE) por si quieren eliminar un autor no se pueda.
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'FraseDb'
        verbose_name_plural = 'Frases'
    
    