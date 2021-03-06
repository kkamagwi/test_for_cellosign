# Generated by Django 3.2.4 on 2021-06-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistical_counters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='clicks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='cost_of_click',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
