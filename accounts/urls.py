from django.urls import path
from . import views 

urlpatterns = [

    #login urls
    path('login/', views.login_view, name='login'),

    #home url
    path('', views.home_view, name='home'),

    path('signup/',views.signup_view, name='signup'),

    path('howitworks/', views.howitworks_view, name='howitworks'),

    path('forclients/', views.for_clients_view, name='forclients'),

    path('browsejob/', views.browse_job_view, name='browsejob'),

    path('forfreelancer/', views.for_freelancer_view, name='forfreelancer'),
]