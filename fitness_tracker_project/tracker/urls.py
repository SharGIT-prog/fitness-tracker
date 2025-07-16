from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('log/', views.log_daily_data, name='log'),
    path('weight-chart/', views.weight_chart_page, name='weight-chart'),
    path('weight-data/', views.weight_data_json, name='weight-data'),
]
