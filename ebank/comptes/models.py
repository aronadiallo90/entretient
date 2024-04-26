from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class CompteBancaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_compte = models.CharField(max_length=50)
    solde = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_compte
