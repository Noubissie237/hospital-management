# Generated by Django 4.2.6 on 2023-12-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]