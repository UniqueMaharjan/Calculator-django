from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_data, name = "index"),
    path('operation',views.operation, name = "operation" )
    ]