# Generated by Django 2.0.9 on 2018-11-08 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0008_auto_20181107_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField(default=2018)),
                ('south_r1_g1_correct', models.BooleanField()),
                ('south_r1_g2_correct', models.BooleanField()),
                ('south_r1_g3_correct', models.BooleanField()),
                ('south_r1_g4_correct', models.BooleanField()),
                ('south_r1_g5_correct', models.BooleanField()),
                ('south_r1_g6_correct', models.BooleanField()),
                ('south_r1_g7_correct', models.BooleanField()),
                ('south_r1_g8_correct', models.BooleanField()),
                ('west_r1_g1_correct', models.BooleanField()),
                ('west_r1_g2_correct', models.BooleanField()),
                ('west_r1_g3_correct', models.BooleanField()),
                ('west_r1_g4_correct', models.BooleanField()),
                ('west_r1_g5_correct', models.BooleanField()),
                ('west_r1_g6_correct', models.BooleanField()),
                ('west_r1_g7_correct', models.BooleanField()),
                ('west_r1_g8_correct', models.BooleanField()),
                ('east_r1_g1_correct', models.BooleanField()),
                ('east_r1_g2_correct', models.BooleanField()),
                ('east_r1_g3_correct', models.BooleanField()),
                ('east_r1_g4_correct', models.BooleanField()),
                ('east_r1_g5_correct', models.BooleanField()),
                ('east_r1_g6_correct', models.BooleanField()),
                ('east_r1_g7_correct', models.BooleanField()),
                ('east_r1_g8_correct', models.BooleanField()),
                ('midwest_r1_g1_correct', models.BooleanField()),
                ('midwest_r1_g2_correct', models.BooleanField()),
                ('midwest_r1_g3_correct', models.BooleanField()),
                ('midwest_r1_g4_correct', models.BooleanField()),
                ('midwest_r1_g5_correct', models.BooleanField()),
                ('midwest_r1_g6_correct', models.BooleanField()),
                ('midwest_r1_g7_correct', models.BooleanField()),
                ('midwest_r1_g8_correct', models.BooleanField()),
                ('south_r2_g1_correct', models.BooleanField()),
                ('south_r2_g2_correct', models.BooleanField()),
                ('south_r2_g3_correct', models.BooleanField()),
                ('south_r2_g4_correct', models.BooleanField()),
                ('west_r2_g1_correct', models.BooleanField()),
                ('west_r2_g2_correct', models.BooleanField()),
                ('west_r2_g3_correct', models.BooleanField()),
                ('west_r2_g4_correct', models.BooleanField()),
                ('east_r2_g1_correct', models.BooleanField()),
                ('east_r2_g2_correct', models.BooleanField()),
                ('east_r2_g3_correct', models.BooleanField()),
                ('east_r2_g4_correct', models.BooleanField()),
                ('midwest_r2_g1_correct', models.BooleanField()),
                ('midwest_r2_g2_correct', models.BooleanField()),
                ('midwest_r2_g3_correct', models.BooleanField()),
                ('midwest_r2_g4_correct', models.BooleanField()),
                ('south_ss_g1_correct', models.BooleanField()),
                ('south_ss_g2_correct', models.BooleanField()),
                ('west_ss_g1_correct', models.BooleanField()),
                ('west_ss_g2_correct', models.BooleanField()),
                ('east_ss_g1_correct', models.BooleanField()),
                ('east_ss_g2_correct', models.BooleanField()),
                ('midwest_ss_g1_correct', models.BooleanField()),
                ('midwest_ss_g2_correct', models.BooleanField()),
                ('south_ee_correct', models.BooleanField()),
                ('west_ee_correct', models.BooleanField()),
                ('east_ee_correct', models.BooleanField()),
                ('midwest_ee_correct', models.BooleanField()),
                ('ff_g1_correct', models.BooleanField()),
                ('ff_g2_correct', models.BooleanField()),
                ('championship_correct', models.BooleanField()),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='championship_id', to='basketball.Team')),
                ('east_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_1_id', to='basketball.Team')),
                ('east_10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_10_id', to='basketball.Team')),
                ('east_11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_11_id', to='basketball.Team')),
                ('east_12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_12_id', to='basketball.Team')),
                ('east_13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_13_id', to='basketball.Team')),
                ('east_14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_14_id', to='basketball.Team')),
                ('east_15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_15_id', to='basketball.Team')),
                ('east_16', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_16_id', to='basketball.Team')),
                ('east_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_2_id', to='basketball.Team')),
                ('east_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_3_id', to='basketball.Team')),
                ('east_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_4_id', to='basketball.Team')),
                ('east_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_5_id', to='basketball.Team')),
                ('east_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_6_id', to='basketball.Team')),
                ('east_7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_7_id', to='basketball.Team')),
                ('east_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_8_id', to='basketball.Team')),
                ('east_9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_9_id', to='basketball.Team')),
                ('east_ee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_ee_id', to='basketball.Team')),
                ('east_r1_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g1_id', to='basketball.Team')),
                ('east_r1_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g2_id', to='basketball.Team')),
                ('east_r1_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g3_id', to='basketball.Team')),
                ('east_r1_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g4_id', to='basketball.Team')),
                ('east_r1_g5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g5_id', to='basketball.Team')),
                ('east_r1_g6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g6_id', to='basketball.Team')),
                ('east_r1_g7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g7_id', to='basketball.Team')),
                ('east_r1_g8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r1_g8_id', to='basketball.Team')),
                ('east_r2_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r2_g1_id', to='basketball.Team')),
                ('east_r2_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r2_g2_id', to='basketball.Team')),
                ('east_r2_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r2_g3_id', to='basketball.Team')),
                ('east_r2_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_r2_g4_id', to='basketball.Team')),
                ('east_ss_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_ss_g1_id', to='basketball.Team')),
                ('east_ss_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east_ss_g2_id', to='basketball.Team')),
                ('ff_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ff_g1_id', to='basketball.Team')),
                ('ff_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ff_g2_id', to='basketball.Team')),
                ('midwest_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_1_id', to='basketball.Team')),
                ('midwest_10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_10_id', to='basketball.Team')),
                ('midwest_11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_11_id', to='basketball.Team')),
                ('midwest_12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_12_id', to='basketball.Team')),
                ('midwest_13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_13_id', to='basketball.Team')),
                ('midwest_14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_14_id', to='basketball.Team')),
                ('midwest_15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_15_id', to='basketball.Team')),
                ('midwest_16', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_16_id', to='basketball.Team')),
                ('midwest_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_2_id', to='basketball.Team')),
                ('midwest_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_3_id', to='basketball.Team')),
                ('midwest_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_4_id', to='basketball.Team')),
                ('midwest_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_5_id', to='basketball.Team')),
                ('midwest_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_6_id', to='basketball.Team')),
                ('midwest_7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_7_id', to='basketball.Team')),
                ('midwest_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_8_id', to='basketball.Team')),
                ('midwest_9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_9_id', to='basketball.Team')),
                ('midwest_ee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_ee_id', to='basketball.Team')),
                ('midwest_r1_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g1_id', to='basketball.Team')),
                ('midwest_r1_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g2_id', to='basketball.Team')),
                ('midwest_r1_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g3_id', to='basketball.Team')),
                ('midwest_r1_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g4_id', to='basketball.Team')),
                ('midwest_r1_g5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g5_id', to='basketball.Team')),
                ('midwest_r1_g6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g6_id', to='basketball.Team')),
                ('midwest_r1_g7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g7_id', to='basketball.Team')),
                ('midwest_r1_g8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r1_g8_id', to='basketball.Team')),
                ('midwest_r2_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r2_g1_id', to='basketball.Team')),
                ('midwest_r2_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r2_g2_id', to='basketball.Team')),
                ('midwest_r2_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r2_g3_id', to='basketball.Team')),
                ('midwest_r2_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_r2_g4_id', to='basketball.Team')),
                ('midwest_ss_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_ss_g1_id', to='basketball.Team')),
                ('midwest_ss_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midwest_ss_g2_id', to='basketball.Team')),
                ('south_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_1_id', to='basketball.Team')),
                ('south_10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_10_id', to='basketball.Team')),
                ('south_11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_11_id', to='basketball.Team')),
                ('south_12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_12_id', to='basketball.Team')),
                ('south_13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_13_id', to='basketball.Team')),
                ('south_14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_14_id', to='basketball.Team')),
                ('south_15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_15_id', to='basketball.Team')),
                ('south_16', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_16_id', to='basketball.Team')),
                ('south_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_2_id', to='basketball.Team')),
                ('south_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_3_id', to='basketball.Team')),
                ('south_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_4_id', to='basketball.Team')),
                ('south_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_5_id', to='basketball.Team')),
                ('south_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_6_id', to='basketball.Team')),
                ('south_7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_7_id', to='basketball.Team')),
                ('south_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_8_id', to='basketball.Team')),
                ('south_9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_9_id', to='basketball.Team')),
                ('south_ee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_ee_id', to='basketball.Team')),
                ('south_r1_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g1_id', to='basketball.Team')),
                ('south_r1_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g2_id', to='basketball.Team')),
                ('south_r1_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g3_id', to='basketball.Team')),
                ('south_r1_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g4_id', to='basketball.Team')),
                ('south_r1_g5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g5_id', to='basketball.Team')),
                ('south_r1_g6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g6_id', to='basketball.Team')),
                ('south_r1_g7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g7_id', to='basketball.Team')),
                ('south_r1_g8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r1_g8_id', to='basketball.Team')),
                ('south_r2_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r2_g1_id', to='basketball.Team')),
                ('south_r2_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r2_g2_id', to='basketball.Team')),
                ('south_r2_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r2_g3_id', to='basketball.Team')),
                ('south_r2_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_r2_g4_id', to='basketball.Team')),
                ('south_ss_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_ss_g1_id', to='basketball.Team')),
                ('south_ss_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='south_ss_g2_id', to='basketball.Team')),
                ('west_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_1_id', to='basketball.Team')),
                ('west_10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_10_id', to='basketball.Team')),
                ('west_11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_11_id', to='basketball.Team')),
                ('west_12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_12_id', to='basketball.Team')),
                ('west_13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_13_id', to='basketball.Team')),
                ('west_14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_14_id', to='basketball.Team')),
                ('west_15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_15_id', to='basketball.Team')),
                ('west_16', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_16_id', to='basketball.Team')),
                ('west_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_2_id', to='basketball.Team')),
                ('west_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_3_id', to='basketball.Team')),
                ('west_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_4_id', to='basketball.Team')),
                ('west_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_5_id', to='basketball.Team')),
                ('west_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_6_id', to='basketball.Team')),
                ('west_7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_7_id', to='basketball.Team')),
                ('west_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_8_id', to='basketball.Team')),
                ('west_9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_9_id', to='basketball.Team')),
                ('west_ee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_ee_id', to='basketball.Team')),
                ('west_r1_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g1_id', to='basketball.Team')),
                ('west_r1_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g2_id', to='basketball.Team')),
                ('west_r1_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g3_id', to='basketball.Team')),
                ('west_r1_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g4_id', to='basketball.Team')),
                ('west_r1_g5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g5_id', to='basketball.Team')),
                ('west_r1_g6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g6_id', to='basketball.Team')),
                ('west_r1_g7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g7_id', to='basketball.Team')),
                ('west_r1_g8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r1_g8_id', to='basketball.Team')),
                ('west_r2_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r2_g1_id', to='basketball.Team')),
                ('west_r2_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r2_g2_id', to='basketball.Team')),
                ('west_r2_g3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r2_g3_id', to='basketball.Team')),
                ('west_r2_g4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_r2_g4_id', to='basketball.Team')),
                ('west_ss_g1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_ss_g1_id', to='basketball.Team')),
                ('west_ss_g2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west_ss_g2_id', to='basketball.Team')),
            ],
        ),
    ]
