# Generated by Django 2.0.6 on 2018-07-17 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanevaluationsabcomparison',
            name='hit',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='humanevaluationsabcomparison',
            name='mturk_run_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orm.HumanEvaluations'),
        ),
        migrations.AlterField(
            model_name='humanevaluationsabcomparison',
            name='prompt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orm.EvaluationDatasetText'),
        ),
    ]