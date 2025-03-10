# Generated by Django 5.0.6 on 2024-07-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnss', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsvdata',
            name='azimuth_1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='azimuth_2',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='azimuth_3',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='azimuth_4',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='elevation_deg_1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='elevation_deg_2',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='elevation_deg_3',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='elevation_deg_4',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='snr_1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='snr_2',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='snr_3',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='snr_4',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='sv_prn_num_1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='sv_prn_num_2',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='sv_prn_num_3',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gsvdata',
            name='sv_prn_num_4',
            field=models.IntegerField(max_length=100),
        ),
    ]
