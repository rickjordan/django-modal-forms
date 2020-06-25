from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('form-data/<name>/', views.get_form_data),
    path('form-data/<name>/<int:pk>', views.get_form_data),

    path('', views.index),
    path('bootstrap/<int:bs_version>/basic', views.basic_example),
    path('bootstrap/<int:bs_version>/datatables', views.datatables),
]
