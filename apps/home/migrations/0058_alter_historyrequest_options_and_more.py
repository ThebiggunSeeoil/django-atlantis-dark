# Generated by Django 4.0.4 on 2022-06-03 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_alter_historyrequest_historyuserposition_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyrequest',
            options={'ordering': ('-HistoryTimeStramp',), 'verbose_name': 'ประวัติการทำรายการ', 'verbose_name_plural': 'ข้อมูลประวัติการทำรายงาน'},
        ),
        migrations.RenameField(
            model_name='stationprofile',
            old_name='station_active',
            new_name='station_activate',
        ),
    ]
