from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('mf-data/<name>/', views.mf_data),
    path('mf-data/<name>/<int:pk>', views.mf_data),

    path('', views.index),
    path('bootstrap/<int:bs_version>/basic', views.basic_example),
    path('bootstrap/<int:bs_version>/datatables', views.datatables),
]
