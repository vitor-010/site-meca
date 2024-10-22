from django.contrib import admin
from django.urls import path, include 
from agendamento import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("agendamento/", include("agendamento.urls"))
]
