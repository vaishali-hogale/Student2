# Generated by Django 5.1.3 on 2024-12-03 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_staff_notification_status_delete_staff_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_notification',
            name='status',
        ),
    ]