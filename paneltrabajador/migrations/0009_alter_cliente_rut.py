# Generated by Django 4.2.7 on 2023-11-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paneltrabajador', '0008_alter_cliente_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
