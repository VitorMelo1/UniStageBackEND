from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('testCreateCompany/', views.cadastrationCompany, name='cadastrationCompany'),
    path('listUser/', views.listUser, name='listUser'),
    path('listCompany/', views.listCompany, name='listCompany'),
    path('listTelephone/', views.listTelephone, name='listTelephone'),
    path('listAdress/', views.listAdress, name='listAdress'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]