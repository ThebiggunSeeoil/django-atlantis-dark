# Generated by Django 4.0.4 on 2022-05-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_user_select_area_area_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCodeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code_name', models.CharField(blank=True, max_length=255, null=True)),
                ('area_code_type', models.CharField(blank=True, max_length=255, null=True)),
                ('timestramp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ข้อมูล รายละเอียด ID ผู้จัดการเขต',
                'verbose_name_plural': 'ข้อมูล รายละเอียด ID ผู้จัดการเขต',
                'ordering': ('id',),
            },
        ),
    ]
