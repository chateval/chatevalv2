# Generated by Django 2.0.6 on 2018-06-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180622_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
