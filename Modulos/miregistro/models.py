from django.db import models

# Create your models here.

class Cliente(models.Model):
    idC = models.CharField(max_length=20, primary_key=True, verbose_name="Cliente")
    Nombre = models.CharField(max_length=20)
    fecha_r = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        txt = "ID-{0}, {1}"
        return txt.format(self.idC, self.Nombre, self.fecha_r)

class Pedido(models.Model):
    Carta = [
        (10000, 'Perro                   $ 10000 '),
        (20000, 'Hamburguesa             $ 20000 '),
        (30000, 'Arroz                   $ 30000'),
    ]
    id = models.AutoField(primary_key=True, verbose_name="ID")
    id_C = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Cliente")
    Precio = models.IntegerField(default=0, choices=Carta)
    Efectivo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Devolucion = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_p = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def save(self, *args, **kwargs):
        self.Devolucion = self.Precio - self.Efectivo

        super(Pedido, self).save(*args, **kwargs)

    def __str__(self):
        txt = "/{0}- {1}/"
        return txt.format(self.Precio, self.Devolucion)