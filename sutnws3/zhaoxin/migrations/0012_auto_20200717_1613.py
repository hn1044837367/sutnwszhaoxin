# Generated by Django 2.2.12 on 2020-07-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhaoxin', '0011_studentad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='evaluation',
            field=models.TextField(db_column='evaluation', default='本人没写自我评价，对自己还是理解不到位啊', null=True, verbose_name='自我评价'),
        ),
    ]