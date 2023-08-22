from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("async/", views.async_view, name="async_view"),
    path("suggestions/",views.suggestions, name="suggestions"),
    path("helper/",views.http_call_async, name="helper")
]