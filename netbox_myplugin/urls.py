from django.urls import path
from . import views

urlpatterns = [
    path('add-device/', views.CustomDeviceCreateView.as_view(), name='custom_device_add'),
    path('edit-device/<int:pk>/', views.CustomDeviceEditView.as_view(), name='custom_device_edit'),

]