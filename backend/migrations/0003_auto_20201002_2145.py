# Generated by Django 3.1 on 2020-10-03 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200927_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='carpa',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='estacionamiento',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='sombrilla',
        ),
        migrations.AlterField(
            model_name='carpa',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservadetalle',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='backend.reserva'),
        ),
        migrations.AlterField(
            model_name='sombrilla',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
