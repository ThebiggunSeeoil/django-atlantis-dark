# Generated by Django 4.0.4 on 2022-05-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_rename_apporove_new_site_manager_notifybyrequest_request_approve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifybyrequest',
            old_name='request_approve',
            new_name='approve_type',
        ),
        migrations.AddField(
            model_name='notifybyrequest',
            name='approve_list',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
