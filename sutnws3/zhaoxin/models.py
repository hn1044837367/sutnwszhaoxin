from django.db import models

# Create your models here.
class Student(models.Model):
    """学生类"""
    
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='编号')
    name = models.CharField(null=True,max_length=20,db_column='name', verbose_name='姓名')
    sex = models.CharField(null=True,max_length=20,db_column='sex', verbose_name='性别')
    studentid = models.CharField(null=True,max_length=20,db_column='studentid', verbose_name='学号')
    subject = models.CharField(null=True,max_length=20,db_column='subject', verbose_name='学院专业')
    phone = models.CharField(null=True,max_length=20,db_column='phone', verbose_name='联系方式')
    qq = models.CharField(null=True,max_length=20,db_column='qq', verbose_name='qq')
    evaluation = models.TextField(null=True,default='本人没写自我评价，对自己还是理解不到位啊',db_column='evaluation', verbose_name='自我评价')
    first = models.CharField(null=True,max_length=20,default='技术部',db_column='first', verbose_name='第一选择')
    second = models.CharField(null=True,max_length=20,default='采编部',db_column='second', verbose_name='第二选择')
    third = models.CharField(null=True,max_length=20,default='外事部',db_column='third', verbose_name='第三选择')
    command = models.TextField(null=True,default='面试官没写对他的评价，你可以看名字去猜是什么样子的样的人',db_column='command', verbose_name='面试官评价')
    interview = models.TextField(default='面试官没写自己是谁，所以我也不知道写谁哦',db_column='interview', verbose_name='面试官')
    st = models.CharField(null=True,max_length=20,default='',db_column='st', verbose_name='被录取状态')
    nowsta = models.CharField(null=True,max_length=20,default='',db_column='nowst', verbose_name='现被选部门')
    finaldepartment = models.CharField(null=True,max_length=20,db_column='finaldepartment', verbose_name='最终入选部门')
    class Meta:
        db_table = 'studentlist'

class StudentAd(models.Model):
    """用户"""
    name     = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    class Meta:
        db_table = 'tb_user'