# Generated by Django 4.1.7 on 2023-03-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='edad',
            field=models.IntegerField(verbose_name=2),
        ),
    ]
