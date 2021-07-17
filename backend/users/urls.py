from django.urls import path
from .views import MeView, user_detail, FavsView, UsersView

app_name = "users"

urlpatterns = [
    path("", UsersView.as_view()),
    path("me/", MeView.as_view()),
    path("me/fav/", FavsView.as_view()),
    path("<int:pk>/", user_detail),
]
