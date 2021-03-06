# Generated by Django 2.2.12 on 2020-07-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhaoxin', '0003_auto_20200715_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='command',
            field=models.CharField(db_column='command', default='本人没写', max_length=20, null=True, verbose_name='面试官评价'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(db_column='department', max_length=20, null=True, verbose_name='入选部门'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first',
            field=models.CharField(db_column='first', default='技术部', max_length=20, null=True, verbose_name='第一选择'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(db_column='id', default=0, primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(db_column='name', max_length=20, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(db_column='phone', max_length=20, null=True, verbose_name='联系方式'),
        ),
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(db_column='qq', max_length=20, null=True, verbose_name='qq'),
        ),
        migrations.AlterField(
            model_name='student',
            name='second',
            field=models.CharField(db_column='second', default='采编部', max_length=20, null=True, verbose_name='第二选择'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(db_column='sex', max_length=20, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='st',
            field=models.CharField(db_column='st', default='', max_length=20, null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentid',
            field=models.CharField(db_column='studentid', max_length=20, null=True, verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.CharField(db_column='subject', max_length=20, null=True, verbose_name='学院专业'),
        ),
        migrations.AlterField(
            model_name='student',
            name='third',
            field=models.CharField(db_column='third', default='外事部', max_length=20, null=True, verbose_name='第三选择'),
        ),
    ]
