# Generated by Django 2.2.12 on 2020-07-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhaoxin', '0004_auto_20200716_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='interviewer',
            new_name='interview',
        ),
    ]