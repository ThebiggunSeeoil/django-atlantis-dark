# Generated by Django 4.0.4 on 2022-05-19 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_multistationtackcare_multi_manager_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multistationtackcare',
            old_name='multi_manager_id',
            new_name='multi_manager_number',
        ),
        migrations.RenameField(
            model_name='multistationtackcare',
            old_name='multi_station_id',
            new_name='multi_station_number',
        ),
    ]
