# Generated by Django 4.0.4 on 2022-05-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_multistationtackcare_deactive_ime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multistationtackcare',
            name='active_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
