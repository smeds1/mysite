# Generated by Django 2.0.9 on 2018-11-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basketball', '0005_auto_20181107_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_alias', models.CharField(max_length=4)),
                ('school_mascot', models.CharField(max_length=50)),
                ('conference', models.CharField(choices=[('AE', 'America East'), ('AAC', 'American Athletic'), ('A10', 'Atlantic 10'), ('ACC', 'Atlantic Coast'), ('AS', 'Atlantic Sun'), ('BIG12', 'Big 12'), ('BIGEAST', 'Big East'), ('BIGSKY', 'Big Sky'), ('BIGSOUTH', 'Big South'), ('BIG10', 'Big Ten'), ('BIGWEST', 'Big West'), ('COLONIAL', 'Colonial'), ('CUSA', 'Conference USA'), ('HORIZON', 'Horizon'), ('IVY', 'Ivy'), ('MAAC', 'Metro Atlantic Athletic'), ('MEAC', 'Mid Eastern Athletic'), ('MAC', 'Mid-American'), ('MVC', 'Missouri Valley'), ('MWC', 'Mountain West'), ('NE', 'Northeast'), ('OVC', 'Ohio Valley'), ('PAC12', 'Pacific 12'), ('PATRIOT', 'Patriot League'), ('SEC', 'Southeastern'), ('SOUTHERN', 'Southern'), ('SOUTHLAND', 'Southland'), ('SWAC', 'Southwestern Athletic'), ('SUMMIT', 'Summit League'), ('SUNBELT', 'Sun Belt'), ('WCC', 'West Coast'), ('WAC', 'Western Athletic')], max_length=10)),
                ('venue_city', models.CharField(max_length=20)),
                ('venue_state', models.CharField(choices=[('AL', 'AL'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'), ('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MS', 'MS'), ('MT', 'MT'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'), ('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], max_length=2)),
                ('venue_name', models.CharField(max_length=50)),
                ('venue_capacity', models.IntegerField()),
            ],
        ),
    ]