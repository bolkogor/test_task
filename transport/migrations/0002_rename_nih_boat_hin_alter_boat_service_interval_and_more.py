# Generated by Django 4.1.5 on 2023-01-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='NIH',
            new_name='HIN',
        ),
        migrations.AlterField(
            model_name='boat',
            name='service_interval',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boat',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='boat',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='VIN',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='service_interval',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='truck',
            name='VIN',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='bed_length',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='truck',
            name='seats',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='truck',
            name='service_interval',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='truck',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]