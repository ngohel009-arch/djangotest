
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('show1/',views.show1,name='show1'),
    path('form1/',views.form1,name='form1'),
    path('getform1/',views.getform1,name='getform1'),
    path('disp/',views.disp,name='disp'),
    path('home/',views.home,name='home'),
    path('memberlogin/', views.memberlogin, name='memberlogin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogin1/', views.adminlogin1, name='adminlogin1'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('adminmember/', views.adminmember, name='adminmember'),
    path('adminaddmember/', views.adminaddmember, name='adminaddmember'),
    path('adminplan/', views.adminplan, name='adminplan'),
    path('adminaddplan/', views.adminaddplan, name='adminaddplan'),
    path('addplan1/', views.addplan1, name='addplan1'),
    path('admintrainers/', views.admintrainers, name='admintrainers'),
    path('adminaddtrainers/', views.adminaddtrainers, name='adminaddtrainers'),
    path('addtrainer/', views.addtrainer, name='addtrainer'),
    path('adminpayment/', views.adminpayment, name='adminpayment'),
    path('adminrecordpayment/', views.adminrecordpayment, name='adminrecordpayment'),
    path('adminattendance/', views.adminattendance, name='adminattendance'),
    path('adminmarkattendance/', views.adminmarkattendance, name='adminmarkattendance'),
    path('adminequipment/', views.adminequipment, name='adminequipment'),
    path('adminaddequipment/', views.adminaddequipment, name='adminaddequipment'),
    path('adminenquiries/', views.adminenquiries, name='adminenquiries'),
    path('adminworkoutplans/', views.adminworkoutplans, name='adminworkoutplans'),
    path('adminaddworkoutplans/', views.adminaddworkoutplans, name='adminaddworkoutplans'),
    path('adminfeedback/', views.adminfeedback, name='adminfeedback'),
    path('memberdashboard/', views.memberdashboard, name='memberdashboard'),
    path('memberprofile/', views.memberprofile, name='memberprofile'),
    path('memberchangepassword/', views.memberchangepassword, name='memberchangepassword'),
]