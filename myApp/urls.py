from django.urls import path
from .views import HomePageView, form_view

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("form/", form_view, name="form-view")
]