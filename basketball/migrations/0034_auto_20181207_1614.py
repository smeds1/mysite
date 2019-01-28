# Generated by Django 2.0.9 on 2018-12-08 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0033_auto_20181207_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_losses',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_region',
            field=models.CharField(choices=[('EAST', 'East'), ('MIDWEST', 'Midwest'), ('SOUTH', 'South'), ('SOUTHEAST', 'Southeast'), ('SOUTHWEST', 'Southwest'), ('WEST', 'West')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_seed',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='season_stats',
            name='tournament_wins',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]