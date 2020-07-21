from django.urls import path

from zhaoxin import views

urlpatterns = [

    path('select/', views.select),

    path('apply/', views.apply),
    path('s/', views.s,name='s'),
    
    path('rename/', views.rename),
    path('register/', views.register,name='register'),
    path('erweima/', views.erweima,name='erweima'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('luquciren/', views.luquciren,name='luquciren'),
    path('jujueciren/', views.jujueciren,name='jujueciren'),
    path('mianshiwancheng/', views.mianshiwancheng,name='mianshiwancheng'),
    path('yimianshi/', views.yimianshi,name='yimianshi'),
    path('yixuanrenyuan/', views.yixuanrenyuan,name='yixuanrenyuan'),
    path('luoxuanrenyuan/', views.luoxuanrenyuan,name='luoxuanrenyuan'),
    path('daimianshi/', views.daimianshi,name='daimianshi'),
]
