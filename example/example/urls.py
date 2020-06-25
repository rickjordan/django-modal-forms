from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('form-data/<name>/', views.get_form_data),
    path('form-data/<name>/<int:pk>', views.get_form_data),

    path('', views.index),
    path('bootstrap4/basic', views.bootstrap4_basic),
    path('bootstrap4/datatables', views.bootstrap4_datatables),
    path('bootstrap3/basic', views.bootstrap3_basic),
    path('bootstrap3/datatables', views.bootstrap3_datatables),
]
