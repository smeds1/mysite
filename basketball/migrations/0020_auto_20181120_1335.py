# Generated by Django 2.0.9 on 2018-11-20 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0019_auto_20181116_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elo',
            name='opp',
        ),
        migrations.RemoveField(
            model_name='elo',
            name='team',
        ),
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['-year']},
        ),
        migrations.DeleteModel(
            name='ELO',
        ),
    ]
