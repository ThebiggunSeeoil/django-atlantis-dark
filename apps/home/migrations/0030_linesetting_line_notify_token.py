# Generated by Django 4.0.4 on 2022-05-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_notifybyrequest_need_admin_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='linesetting',
            name='line_notify_token',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
