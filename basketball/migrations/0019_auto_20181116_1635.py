# Generated by Django 2.0.9 on 2018-11-17 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0018_auto_20181114_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('season', models.PositiveSmallIntegerField()),
                ('elo_before', models.PositiveSmallIntegerField()),
                ('elo_after', models.PositiveSmallIntegerField()),
                ('win', models.BooleanField()),
                ('opp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opp_id', to='basketball.Team')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_id', to='basketball.Team')),
            ],
        ),
        migrations.AlterModelOptions(
            name='bracket',
            options={'ordering': ['-year']},
        ),
    ]
