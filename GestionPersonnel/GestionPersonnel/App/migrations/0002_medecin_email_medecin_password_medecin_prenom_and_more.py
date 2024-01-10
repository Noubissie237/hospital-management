# Generated by Django 4.2.6 on 2023-12-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='medecin',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medecin',
            name='prenom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
