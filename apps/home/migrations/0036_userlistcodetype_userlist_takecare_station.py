# Generated by Django 4.0.4 on 2022-05-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_areacodetype_area_notify'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlistcodetype',
            name='userList_takecare_station',
            field=models.CharField(blank=True, default='single', max_length=255, null=True),
        ),
    ]
