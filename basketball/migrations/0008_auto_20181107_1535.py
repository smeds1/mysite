# Generated by Django 2.0.9 on 2018-11-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0007_auto_20181107_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='school_alias',
            field=models.CharField(max_length=5),
        ),
    ]
