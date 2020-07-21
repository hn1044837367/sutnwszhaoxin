# Generated by Django 2.2.12 on 2020-07-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.TextField(db_column='name', verbose_name='姓名')),
                ('sex', models.TextField(db_column='sex', verbose_name='性别')),
                ('studentid', models.TextField(db_column='studentid', verbose_name='学号')),
                ('subject', models.TextField(db_column='subject', verbose_name='学院专业')),
                ('phone', models.TextField(db_column='phone', verbose_name='联系方式')),
                ('qq', models.TextField(db_column='qq', verbose_name='qq')),
                ('evaluation', models.TextField(db_column='evaluation', default='本人没写', verbose_name='自我评价')),
                ('first', models.TextField(db_column='first', default='技术部', verbose_name='第一选择')),
                ('second', models.TextField(db_column='second', default='采编部', verbose_name='第二选择')),
                ('third', models.TextField(db_column='third', default='外事部', verbose_name='第三选择')),
                ('command', models.TextField(db_column='command', default='本人没写', verbose_name='面试官评价')),
                ('department', models.TextField(db_column='department', verbose_name='入选部门')),
                ('interviewer', models.TextField(db_column='interview', default='本人没写', verbose_name='面试官')),
                ('status', models.TextField(db_column='status', default='', verbose_name='状态')),
            ],
            options={
                'db_table': 'studentlist',
            },
        ),
    ]
