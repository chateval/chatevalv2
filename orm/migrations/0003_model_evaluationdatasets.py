# Generated by Django 2.0.7 on 2018-08-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_model_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='evaluationdatasets',
            field=models.ManyToManyField(to='orm.EvaluationDataset'),
        ),
    ]