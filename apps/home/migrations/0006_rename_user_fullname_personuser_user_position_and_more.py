# Generated by Django 4.0.4 on 2022-04-23 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_personuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personuser',
            old_name='user_fullname',
            new_name='user_position',
        ),
        migrations.RemoveField(
            model_name='personuser',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='personuser',
            name='user_lastname',
        ),
    ]
