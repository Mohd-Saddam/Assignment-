# Generated by Django 3.1 on 2020-08-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_auto_20200808_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timezone',
            name='tz',
            field=models.CharField(choices=[('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Kolkata', 'Asia/Kolkata')], max_length=50),
        ),
    ]
