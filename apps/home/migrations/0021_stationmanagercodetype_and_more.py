# Generated by Django 4.0.4 on 2022-05-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_areacodetype_timestramp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationManagerCodeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StationManager_code_name', models.CharField(blank=True, max_length=255, null=True)),
                ('StationManager_code_type', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('StationManager_adddatetime', models.DateTimeField(auto_now_add=True)),
                ('StationManager_register', models.BooleanField(default=False)),
                ('StationManager_register_datetime', models.DateTimeField(blank=True, default=None, null=True)),
                ('StationManager_userid', models.CharField(blank=True, max_length=255, null=True)),
                ('StationManager_display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('StationManager_picture_url', models.URLField()),
                ('StationManager_status_message', models.CharField(blank=True, max_length=255, null=True)),
                ('StationManager_activate', models.BooleanField(default=False)),
                ('StationManager_notify', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ข้อมูล รายละเอียด ID ผู้จัดการเขต',
                'verbose_name_plural': 'ข้อมูล รายละเอียด ID ผู้จัดการเขต',
                'ordering': ('id',),
            },
        ),
        migrations.RenameField(
            model_name='areacodetype',
            old_name='adddatetime',
            new_name='area_adddatetime',
        ),
        migrations.RenameField(
            model_name='areacodetype',
            old_name='register_datetime',
            new_name='area_register_datetime',
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_activate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_display_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_notify',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_picture_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_status_message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='areacodetype',
            name='area_userid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
