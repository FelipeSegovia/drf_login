from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Nombre', max_length=75)
    last_name = models.CharField('Apellidos', max_length=100)
    username = models.CharField('Usuario', max_length=100, unique=True)
    email = models.EmailField('Email', unique=True)
    password = models.CharField('Contraseña', max_length=250)

    class Meta:
        db_table = "user"

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)


