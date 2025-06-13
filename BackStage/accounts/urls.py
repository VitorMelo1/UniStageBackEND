from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.index, name ='index'),
    path('testCreateCompany', views.cadastrationCompany, name = 'cadastrationCompany'),
    #path('listCompany', views.listUserCompany_view, name = 'listCompany'),
    path('listUser', views.listUser, name = 'listUser'),
    path('listCompany', views.listCompany, name = 'listCompany'),
    path('listTelephone', views.listTelephone, name = 'listTelephone'),
    path('listAdress', views.listAdress, name = 'listAdress'),
]