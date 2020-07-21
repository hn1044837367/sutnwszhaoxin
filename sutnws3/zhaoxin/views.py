from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db import models
from zhaoxin.models import Student, StudentAd
import json
import pymysql
from django.contrib.messages.storage import session
from bpmappers.djangomodel import ModelMapper

class SubjectMapper(ModelMapper):
   
    class Meta:
        model = Student


# 新生报名数据存储
def register(request):

    a = request.POST#获取get()请求
    name = a.get('name')
    sex = a.get('sex')
    studentid = a.get('studentid')
    subject = a.get('subject')
    phone = a.get('phone')
    qq = a.get('qq')
    first = a.get('first')
    second = a.get('second')
    third = a.get('third')
    evaluation = a.get('evaluation')
    st='0'
    b = Student(name=name,sex=sex,studentid=studentid,subject=subject,phone=phone,qq=qq,first=first,second=second,third=third,evaluation=evaluation,st=st,nowsta=first)
    b.save()
    data = {'code': 0,}
    return JsonResponse(data)
    
# 新生报名界面渲染
def apply(request):
    return render(request, 'register.html')


# 登录管理界面招新
def login(request):
    """登录"""
    
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        password = form.get('password')
        user = StudentAd.objects.filter(name=name, password=password).first()
        if user:

            # 登录成功后将用户编号和用户名保存在session中
                request.session['user'] = user.name
                us = form.get('name')
                data = {'code': 0,'user':us}
                return JsonResponse(data)
            
        else:
            
            return render(request, 'register.html')

    if request.method == 'GET':
        return render(request, 'login.html')

# 退出登录
def logout(request):
    request.session.flush()
    return redirect('/login')

# 获得所有学生
def select(request):
    
    students =  Student.objects.all()

    return render(request,'index.html',{'students':students})
# 获得特别学生
def s(request):
    ss= request.GET['studentid']
    students = Student.objects.filter(studentid=ss)
    return render(request,'index.html',{'dode':0,'students':students})
    
    



    
# 获得当前部门待面试学生
def daimianshi(request):
    students = Student.objects.filter(nowsta=request.session['user'],st="0")

    return render(request,'index.html',{'students':students})
# 获得当前部门已面试学生
def yimianshi(request):
    students =Student.objects.filter(nowsta=request.session['user'],st="1")

    return render(request,'index.html',{'students':students})


# 获得当前部门已选人员学生
def yixuanrenyuan(request):
    students =Student.objects.filter(nowsta=request.session['user'],st="2")

    return render(request,'index.html',{'students':students})

# 获得落选人员
def luoxuanrenyuan(request):
    students =Student.objects.filter(st="5")

    return render(request,'index.html',{'students':students})



# get请求获得二维码
def erweima(request):
   
    return render(request,'erweima.html')


# 进入个别学生的管理界面
def rename(request):

    try:
        sid = int(request.GET['sid'])
        students = Student.objects.get(id=sid)
        return render(request, 'rename.html', {'students':students})
    except (KeyError, ValueError, Student.DoesNotExist):
        
        return redirect('')

#点击"面试完成"操作

def mianshiwancheng(request):
    ids = int(request.POST['id'])
    students =  Student.objects.filter(nowsta=request.session['user'],st='0')
    now = request.session['user']
    a = request.POST#获取get()请求
    interview= a.get('interview')
    command= a.get('command')
    studen=Student.objects.filter(id=ids)
    studen.update(st='1',nowsta=now,command=command,interview=interview)
    return render(request,'index.html',{'students':students})


#点击"录取此人"操作
def luquciren(request):
    ids = int(request.POST['id'])
    now = request.session['user']
    studen=Student.objects.filter(id=ids)
    a = request.POST#获取get()请求
    interview= a.get('interview')
    command= a.get('command')
    studen.update(st='2',nowsta=now,command=command,interview=interview)
    students =  Student.objects.filter(nowsta=request.session['user'],st='0')
    return render(request,'index.html',{'students':students})


#点击"不录取此人"操作
def jujueciren(request):
    students =  Student.objects.filter(nowsta=request.session['user'],st='0')
    ids = int(request.POST['id'])
    now = request.session['user']
    a = request.POST#获取get()请求
    interview= a.get('interview')
    command= a.get('command')
    studen=Student.objects.filter(id=ids)
    studen.update(st='5',nowsta='未被录取',command=command,interview=interview)
    return render(request,'index.html',{'students':students})
























