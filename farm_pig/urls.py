from django.urls import path

from . import views
app_name = "products"

urlpatterns = [
    path('', views.farm, name="farm"),
    path('birth', views.birth, name="birth"),
]
