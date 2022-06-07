# Generated by Django 4.0.4 on 2022-05-31 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_rename_email_notify_stationprofile_debug_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HistoryPushOrReply', models.CharField(blank=True, max_length=255, null=True)),
                ('HistoryReportTypeRequest', models.CharField(blank=True, max_length=255, null=True)),
                ('HistoryReportDeatil', models.CharField(blank=True, max_length=255, null=True)),
                ('HistoryStatusSend', models.CharField(blank=True, max_length=255, null=True)),
                ('HistoryTimeStramp', models.DateTimeField(auto_now_add=True)),
                ('HistoryUserName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.userlistcodetype')),
                ('HistoryUserPosition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.position')),
                ('HistoryUserStationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.stationprofile')),
            ],
            options={
                'verbose_name': 'ประวัติการทำรายการ',
                'verbose_name_plural': 'ข้อมูลประวัติการทำรายงาน',
                'ordering': ('id',),
            },
        ),
    ]
