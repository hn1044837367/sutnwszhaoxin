# Generated by Django 2.2.12 on 2020-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhaoxin', '0002_auto_20200715_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False, verbose_name='编号'),
        ),
    ]
