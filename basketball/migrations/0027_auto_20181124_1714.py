# Generated by Django 2.0.9 on 2018-11-25 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0026_bracket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bracket',
            name='ff_left',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ff_left_id', to='basketball.Team'),
        ),
        migrations.AlterField(
            model_name='bracket',
            name='ff_right',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ff_right_id', to='basketball.Team'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='top_left_16',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_left_16_id', to='basketball.Team'),
        ),
    ]