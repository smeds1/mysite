# Generated by Django 2.0.9 on 2018-12-13 23:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0037_auto_20181213_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season_stats',
            options={'ordering': ['-year', 'team']},
        ),
        migrations.AlterField(
            model_name='bracket',
            name='year',
            field=models.PositiveSmallIntegerField(default=2018, validators=[django.core.validators.MinValueValidator(1939)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='elo',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='losses',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='ppg',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Points Per Game'),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='ppga',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Points Per Game Against'),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_losses',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_seed',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(16)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_wins',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='wins',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='year',
            field=models.PositiveSmallIntegerField(default=2018, validators=[django.core.validators.MinValueValidator(1939)]),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='year',
            field=models.PositiveSmallIntegerField(default=2018, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(1939)]),
        ),
    ]
