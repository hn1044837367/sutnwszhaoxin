# Generated by Django 2.2.12 on 2020-07-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhaoxin', '0006_auto_20200717_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='command',
            field=models.CharField(db_column='command', default='面试官没写对他的评价，你可以看名字去猜是什么样子的样=人', max_length=20, null=True, verbose_name='面试官评价'),
        ),
        migrations.AlterField(
            model_name='student',
            name='evaluation',
            field=models.TextField(db_column='evaluation', default='本人没写自我评价，对自己还是理解不到位啊', verbose_name='自我评价'),
        ),
        migrations.AlterField(
            model_name='student',
            name='interview',
            field=models.TextField(db_column='interview', default='面试官没写自己是谁，所以我也不知道写谁哦', verbose_name='面试官'),
        ),
    ]