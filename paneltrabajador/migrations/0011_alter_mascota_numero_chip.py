# Generated by Django 4.2.7 on 2023-11-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paneltrabajador', '0010_alter_mascota_numero_chip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='numero_chip',
            field=models.BigIntegerField(unique=True),
        ),
    ]
