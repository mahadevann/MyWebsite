from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ContactUs/', views.contactus,name='contact'),
    path('bloghome/', views.bloghome,name='blog'),
    path('HeaderBar/', views.headerbar,name='hbar'),
    path('your-name/', views.get_name,name='gname'),
    path('blogdetail/', views.blogdetail, name='blogdetail'),
    path('services/', views.services, name='services'),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),

]