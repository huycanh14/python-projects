# Generated by Django 3.0.3 on 2020-04-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200405_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
