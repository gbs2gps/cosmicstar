from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.index1, name='index1'),
    path('3', views.index3, name='index3'),
    path('4', views.index4, name='index4'),
    path('5', views.index5, name='index5'),
    path('6', views.index6, name='index6'),
    path('7', views.index7, name='index7'),
    path('8', views.index8, name='index8'),
    path('9', views.index9, name='index9'),
    path('10', views.index10, name='index10'),
    path('11', views.index11, name='index11'),
    path('13', views.index13, name='index13'),
    path('14', views.index14, name='index14'),
    path('15', views.index15, name='index15'),
    path('16', views.index16, name='index16'),
    path('17', views.index17, name='index17'),
    path('18', views.index18, name='index18'),
    path('19', views.index19, name='index19'),
    path('21', views.index21, name='index21'),
    path('22', views.index22, name='index22'),
    path('23', views.index23, name='index23'),
    path('24', views.index24, name='index24'),
    path('25', views.index25, name='index25'),
    path('26', views.index26, name='index26'),

]