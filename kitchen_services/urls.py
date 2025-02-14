from django.urls import path, include
from kitchen_services.views import index


urlpatterns = [
    path("", index, name="index"),
]

app_name = "restaurant_services"
