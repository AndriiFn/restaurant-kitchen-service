from django.urls import path, include
from kitchen_services.views import index, DishListView, DishTypeListView


urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen_services"
