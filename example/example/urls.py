from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form-data/<name>/', views.get_form_data),
    path('form-data/<name>/<int:pk>', views.get_form_data),
    path('', views.index),
]
