# Generated by Django 5.0.6 on 2024-07-30 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnss', '0008_alter_gsvdata_azimuth_1_alter_gsvdata_azimuth_2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GSVData',
        ),
    ]
