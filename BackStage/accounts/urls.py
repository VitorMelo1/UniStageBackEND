from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('testCreateCompany', views.cadastrationCompany, name = 'cadastrationCompany'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('listCompany', views.listUserCompany_view, name = 'listCompany'),
    path('listUser', views.listUser, name = 'listUser'),
    path('listCompany', views.listCompany, name = 'listCompany'),
    path('listTelephone', views.listTelephone, name = 'listTelephone'),
    path('listAdress', views.listAdress, name = 'listAdress'),
]