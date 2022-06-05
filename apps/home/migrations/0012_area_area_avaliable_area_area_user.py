# Generated by Django 4.0.4 on 2022-04-23 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_personuser_user_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='area_avaliable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='area',
            name='area_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.personuser'),
        ),
    ]
