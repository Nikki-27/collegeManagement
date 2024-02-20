from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('erp.urls')),
    path('erp/', include('erp.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='erp/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='erp/logout.html'), name='logout'),
]
