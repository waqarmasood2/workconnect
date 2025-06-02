# urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views
from .views import AdminDashboardView

urlpatterns = [
    path('', login_required(AdminDashboardView.as_view()), name='wcadmin_dashboard'),
    # Add other admin URLs as needed
]