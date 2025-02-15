from django.urls import path, include
from kitchen_services.views import index, DishListView


urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "kitchen_services"
