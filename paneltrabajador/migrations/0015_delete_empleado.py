# Generated by Django 4.2.7 on 2023-11-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paneltrabajador', '0014_remove_empleado_id_alter_empleado_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
