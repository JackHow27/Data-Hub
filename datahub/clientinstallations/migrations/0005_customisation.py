# Generated by Django 4.1.7 on 2023-05-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientinstallations', '0004_alter_applicationinstance_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('adolink', models.CharField(max_length=100)),
                ('ticketlink', models.CharField(max_length=100)),
            ],
        ),
    ]
