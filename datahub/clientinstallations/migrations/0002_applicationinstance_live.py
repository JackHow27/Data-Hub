# Generated by Django 4.1.7 on 2023-05-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientinstallations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationinstance',
            name='live',
            field=models.BooleanField(default=False),
        ),
    ]
