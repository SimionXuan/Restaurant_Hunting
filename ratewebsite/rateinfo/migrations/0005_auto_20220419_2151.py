# Generated by Django 3.2.5 on 2022-04-20 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rateinfo', '0004_auto_20220419_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['place_place', 'place_street']},
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_city',
            new_name='place_street',
        ),
    ]
