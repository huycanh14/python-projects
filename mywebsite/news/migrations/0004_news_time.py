# Generated by Django 3.0.3 on 2020-04-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200408_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]
