from apps.category import views
from django.urls import path


urlpatterns = [

    path("categories/", views.Categories.as_view()),
]
