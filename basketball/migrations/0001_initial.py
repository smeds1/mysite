# Generated by Django 2.0.9 on 2018-11-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_mascot', models.CharField(max_length=50)),
            ],
        ),
    ]
