# Generated by Django 4.0.4 on 2022-05-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_areacodetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacodetype',
            name='area_code_type',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
