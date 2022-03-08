
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('tenant/<str:mail>',views.tenant,name='tenant'),
    path('admin1',views.admin1,name='admin1'),
    path('success',views.success,name='success'),
    path('rent/<str:email>',views.rentpay,name='rent'),
    path('complaint/<str:mail>',views.complaint,name='complaint'),
    path('admin_complaint',views.adminmsg,name='admin_complaint'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('sendmail/<str:email>',views.sendmail,name='sendmail'),
    path('admin_visitor',views.visitor,name='admin_visitor'),
    path('sendmail_visitor/<str:email>',views.sendmail_visitor,name='sendmail_visitor'),
    path('delete_visitor/<int:id>',views.delete_visitor,name='delete_visitor')
]