# Generated by Django 5.1.2 on 2024-11-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMammaMia', '0004_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='numero_comensales',
            new_name='npersonas',
        ),
    ]
