# Generated by Django 5.0.6 on 2024-07-29 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnss', '0002_gsv'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GGA',
        ),
        migrations.DeleteModel(
            name='GSA',
        ),
        migrations.DeleteModel(
            name='GSV',
        ),
    ]
