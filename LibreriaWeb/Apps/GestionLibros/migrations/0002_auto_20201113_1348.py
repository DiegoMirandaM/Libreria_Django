# Generated by Django 3.1.2 on 2020-11-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionLibros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Cantidad_Disponible',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libro',
            name='Precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='venta',
            name='Cantidad_Venta',
            field=models.IntegerField(default=0),
        ),
    ]
