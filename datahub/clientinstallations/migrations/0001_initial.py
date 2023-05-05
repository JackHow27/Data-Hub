# Generated by Django 4.1.7 on 2023-05-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shortcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('jobtitle', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='clientinstallations.client')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('ECOI', 'ECOI'), ('CCR', 'CCR'), ('IAR', 'IAR')], max_length=50)),
                ('environment', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('relationshipmanager', models.CharField(blank=True, max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='clientinstallations.client')),
            ],
        ),
    ]
