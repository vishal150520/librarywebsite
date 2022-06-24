from django.urls import path
from . import views
from .views  import adminsignup1,studentlogin1,studentsignup1,adminsignup11,adlog11,admins12,alogout1,addb1,saveb1,updatebook12,updatebook14,delb1,delb2,getallbooks1,back,logout2,stusign1,stulog1,viewall1,stulogout1
urlpatterns = [
    path('',views.home,name='home'),
    path('adminsignup/',views.adminsignup1,name="template1"),
    path('studentlogin',views.studentlogin1,name="template2"),
    path('studentsignup',views.studentsignup1,name="template3"),
    path('adminsignup',views.adminsignup11,name="signupadmin"),
    path('adminlog',views.adlog11,name="adlog"),
    path('adminsucess',views.admins12,name="admins1"),
    path('adminslogout',views.alogout1,name="alogout"),
    path('addbook',views.addb1,name="addbook"),
    path('savebook1',views.saveb1,name="savebook"),
    path('updatebook1',views.updatebook12,name="updatebook"),
    path('update',views.updatebook14,name="updatebook13"),
    path('deletebook',views.delb1,name="deletebook"),
    path('deletebooks',views.delb2,name="delbook"),
    path('allbooks',views.getallbooks1,name="getallbooks"),
    path('back',views.back,name="cm1"),
    path('log-out',views.logout2,name="logout1"),
    path('stu-sign',views.stusign1,name="signupstu"),
    path('stu-log',views.stulog1,name="stulog"),
    path('viewall',views.viewall1,name="viewall"),
    path('student-logout',views.stulogout1,name="stulogout"),
]