# Generated by Django 4.0.4 on 2022-04-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_user_fullname_personuser_user_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personuser',
            name='user_station_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.stationprofile'),
        ),
    ]
