# Generated by Django 4.1.7 on 2023-05-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientinstallations', '0003_servergroup_alter_applicationinstance_product_server_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationinstance',
            name='server',
            field=models.ManyToManyField(to='clientinstallations.server'),
        ),
    ]